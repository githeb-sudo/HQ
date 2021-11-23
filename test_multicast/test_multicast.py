import os,sys,shlex,subprocess,paramiko,argparse,time,pandas
from numpy.random import randint
import numpy as np
from socket import timeout


os.environ['PYTHONUNBUFFERED'] = '1'

settings_id=sys.argv[1][-1]
if (settings_id=='1'):
    parameter=["settings_id","CSV_filename","ipaddrs_range","ports_range","client_ip","username_client","password_client","server_ip","username_server","password_server","ssid_2g","ssid_5g","wifi_password"]
else:    
    parameter=["settings_id","CSV_filename","ipaddrs_range","ports_range","server_mac","username_server","password_server","client_mac","username_client","password_client","ssid_2g","ssid_5g","wifi_password"]
    
parser = argparse.ArgumentParser()


for i in range(len(parameter)):
    parser.add_argument('-'+parameter[i])
namespace = parser.parse_args()
locals().update(namespace.__dict__)


def check_parameter(key,value):
    """
    check the value of a required parameter, alert and exit if not-defined
    """  
    if (value== None):
        sys.exit("-"+key+"parameter has to be set!")

        
def check_all():
    """
    Check that all the required parameters are set
    """  
    required_parameters=namespace.__dict__
    required_parameters.pop('ports_range',"")
    for k,v in required_parameters:
        check_parameter(k,v)

"""
ports parameter is optional. If not specified, it will be a random number between 0 and 102
parse FLAGS.mean_list according to comma

Returns:
    ports (list [str])   : list containing the ports numbers to test 
"""
if (ports_range!=None):
    ports=list(np.arange(ports_range[0],ports_range[1]))
    ports=[str(port) for port in ports ]
else:
    ports=[str(randint(0,1024))]

range_splitted=ipaddrs_range.split('.')
ipaddrs=["224.0.0."+str(i) for i in range(int(range_splitted[3][:(range_splitted[3]).index(',')]),int(range_splitted[-1][:-1]))]



"""
Get IP address when all available is the hardware address


Returns:
    str   : the string value of the ip address associated to the input MAC address
"""
def rarp(mac):
    scan="nmap -sn 192.168.1.0/24"
    subprocess.call(shlex.split(scan))   
    get_arp_table="arp -a"
    grep_ip=" grep "+mac
    arp_table=subprocess.Popen(shlex.split(get_arp_table),stdout=subprocess.PIPE)
    output=str((subprocess.Popen(shlex.split(grep_ip),stdin=arp_table.stdout, stdout=subprocess.PIPE)).communicate())
    return output[output.find("1"):output.find(")")]


if(settings_id=="2"):
    server_ip=rarp(server_mac)
    client_ip=rarp(client_mac)
    
    

"""
Make a connection with the remote devices through SSh2

"""
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(client_ip, username=username_client, password=password_client)


ssh_server = paramiko.SSHClient()
ssh_server.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_server.connect(server_ip, username=username_server, password=password_server)


"""
Wait for a response and, thus synchronise the interaction with the remote shell 
"""
def wait4response(shell):
    while not shell.recv_ready():
        time.sleep(0.5)
    shell.recv(100000)

"""
Wait for an expected response or a specific recurrent error
Wait for a specific wait time (180s)


Returns:
    recovered (str)   : the useful string recovered from the server shell
"""
    
def wait4expected(shell,expected,error):
    shell.settimeout(180)
    try:
        recovered=str(shell.recv(100000))
        while (((recovered.find(expected))==(-1)) and ((recovered.find(error))==(-1))):
            time.sleep(0.5)
            recovered=str(shell.recv(100000))
        if(recovered.find(error)!=(-1)):
            sys.exit("Error:"+error)
        return recovered
    except timeout:
        sys.exit("Timeout error:"+error)
    shell.settimeout(None)
    
"""
Connect the devide to a wifi connection
"""    
def connectWifi(ssid):
        return "nmcli dev wifi connect "+ssid+" password "+wifi_password+"\n"

    
"""
Modify the setting autoconnect, set by default, on the device.
"""
def no_autoconnect(ssid):
        return "nmcli con modify "+ssid+" autoconnect no\n"


combinations=["Eth-Eth","Eth-2.4GHZ","Eth-5GHZ","2.4GHZ-Eth","2.4GHZ-2.4GHZ","2.4GHZ-5GHZ","5GHZ-Eth","5GHZ-2.4GHZ","5GHZ-5GHZ"]

server_shell =ssh_server.invoke_shell()
time.sleep(1)
wait4response(server_shell)


client_shell =ssh_client.invoke_shell()
time.sleep(1)
wait4response(client_shell)

"""
Get root privileges on the remote shell, enable Wi-Fi, connect to an available access points and disable autoconnect setting
"""
def shellnWifi_prepare(shell,passwd):
    shell.send("sudo su\n")
    wait4response(shell)

    shell.send(passwd+"\n")
    wait4response(shell)

    wifion="nmcli r wifi on\n"
    shell.send(wifion)
    wait4response(shell)

    rescan="nmcli device wifi rescan\n"
    shell.send(rescan)
    wait4response(shell)

    if(settings_id=="2"):
        shell.send(connectWifi(ssid_2g))
        wait4expected(shell,"successfully activated","2.4Ghz connection activation failed. Try to manually connect to the wifi or change the wifi channel and try again.")

        shell.send(connectWifi(ssid_5g))
        wait4expected(shell,"successfully activated","5Ghz connection activation failed. Try to manually connect to the wifi or change the wifi channel and try again.")

    shell.send(no_autoconnect(ssid_2g))
    shell.send(no_autoconnect(ssid_5g))

shellnWifi_prepare(client_shell,password_client)   
shellnWifi_prepare(server_shell,password_server)

"""
Connect, as required, to a Wi-Fi network specified by SSID or the LAN
"""
def connect(shell,ssid=-1):
    if(ssid!=(-1)):
        shell.send("nmcli con up "+ssid+"\n")
        wait4expected(shell,"successfully activated",ssid+'activation failed')
    else:
        shell.send("sudo nmcli con down $(nmcli con show -a )\n")
        wait4expected(shell,"Error","No Error is expected")
        #wait4expected(shell,"active connections found","No connection specified.")

        
"""
The core function, to test, for a specific combination, the multicast traffic and write/append the results on the csv output file. 
"""
def test_oneCombination(combinationIndex):
    csv_abspath=os.getcwd()+"/"+CSV_filename
    pandas.DataFrame([[["",combinations[combinationIndex],""]]]).to_csv(csv_abspath,index=False,header=False,mode="a")
    pandas.DataFrame([["ip address","port","loss rate(in %)"]]).to_csv(csv_abspath,index=False,header=False,mode="a")
    for multicastip in ipaddrs:
        for port in ports:
            server="iperf -s -u -B "+multicastip+" -p "+port+" & sleep 4\n"
            server_shell.send(server)
            wait4response(server_shell)
            
            client="iperf -c "+multicastip+" -u -t3 -i1 -T999 -p "+port+"\n"
            ssh_client.exec_command(client)
            
            result=wait4expected(server_shell,'%)','159')
#             result=str(server_shell.recv(100000))
            print(result)
            print("\n\n")
            loss_rate=result[result.rfind("(")+1:result.rfind(")")-1]
            pandas.DataFrame([[multicastip,port,loss_rate]]).to_csv(csv_abspath,index=False,header=False,mode="a")
            
# def test_allCombinations0():
#     combinationIndex=0
#     for ssid_s in [-1]:
#         connect(server_shell,ssid_s)   
#         for ssid_c in [-1]:
#             connect(client_shell,ssid_c)
#             test_oneCombination(combinationIndex)
#             combinationIndex+=1
# def test_allCombinations1():
#     combinationIndex=0
#     for ssid_s in [-1,ssid_5g]:
#         connect(server_shell,ssid_s)   
#         for ssid_c in [-1,ssid_5g]:
#             connect(client_shell,ssid_c)
#             test_oneCombination(combinationIndex)
#             combinationIndex+=1
# test_allCombinations0()
            
def test_allCombinations():
    combinationIndex=0
    for ssid_s in [-1,ssid_2g,ssid_5g]:
        connect(server_shell,ssid_s)   
        for ssid_c in [-1,ssid_2g,ssid_5g]:
            connect(client_shell,ssid_c)
            test_oneCombination(combinationIndex)
            combinationIndex+=1
            
test_allCombinations()

ssh_server.close()
ssh_client.close()
