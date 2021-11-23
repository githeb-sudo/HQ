import os,sys,shlex,subprocess,paramiko,argparse,time,pandas
from numpy.random import randint
import numpy as np
from socket import timeout

combinations=["Eth-Eth","Eth-2.4GHZ","Eth-5GHZ","2.4GHZ-Eth","2.4GHZ-2.4GHZ","2.4GHZ-5GHZ","5GHZ-Eth","5GHZ-2.4GHZ","5GHZ-5GHZ"]

def check_parameter(key,value):
    """
    check the value of a required parameter, alert and exit if not-defined
    """  
    if (value== None):
        sys.exit("-"+key+"parameter has to be set!")


        
def check_all(required_parameters):
    """
    Check that all the required parameters are set
    """  
    for k,v in required_parameters.items():
        check_parameter(k,v)



def rarp(mac):
    """
    Get IP address when all available is the hardware address


    Returns:
        str   : the string value of the ip address associated to the input MAC address
    """
    scan="nmap -sn 192.168.1.0/24"
    subprocess.call(shlex.split(scan))   
    get_arp_table="arp -a"
    grep_ip=" grep "+mac
    arp_table=subprocess.Popen(shlex.split(get_arp_table),stdout=subprocess.PIPE)
    output=str((subprocess.Popen(shlex.split(grep_ip),stdin=arp_table.stdout, stdout=subprocess.PIPE)).communicate())
    return output[output.find("1"):output.find(")")]



def wait4response(shell):
    """
    Wait for a response and, thus synchronise the interaction with the remote shell 
    """
    while not shell.recv_ready():
        time.sleep(0.5)
    shell.recv(100000)


    
def wait4expected(shell,expected,error):
    """
    Wait for an expected response or a specific recurrent error
    Wait for a specific wait time (180s)


    Returns:
        recovered (str)   : the useful string recovered from the server shell
    """
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
    
    
def connectWifi(ssid,wifi_password):
    """
    Connect the devide to a wifi connection
    """
    return "nmcli dev wifi connect "+ssid+" password "+wifi_password+"\n"

    

def no_autoconnect(ssid):
    """
    Modify the setting autoconnect, set by default, on the device.
    """
    return "nmcli con modify "+ssid+" autoconnect no\n"



def shellnWifi_prepare(shell,passwd,settings_id,ssid_2g,ssid_5g,wifi_password):
    """
    Get root privileges on the remote shell, enable Wi-Fi, connect to an available access points and disable autoconnect setting
    """
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
        shell.send(connectWifi(ssid_2g,wifi_password))
        wait4expected(shell,"successfully activated","2.4Ghz connection activation failed. Try to manually connect to the wifi or change the wifi channel and try again.")

        shell.send(connectWifi(ssid_5g,wifi_password))
        wait4expected(shell,"successfully activated","5Ghz connection activation failed. Try to manually connect to the wifi or change the wifi channel and try again.")

    shell.send(no_autoconnect(ssid_2g))
    shell.send(no_autoconnect(ssid_5g))



def connect(shell,ssid=-1):
    """
    Connect, as required, to a Wi-Fi network specified by SSID or the LAN
    """
    if(ssid!=(-1)):
        shell.send("nmcli con up "+ssid+"\n")
        wait4expected(shell,"successfully activated",ssid+'activation failed')
    else:
        shell.send("sudo nmcli con down $(nmcli con show | grep '802-11-wireless' )\n")
        wait4response(shell)
        #wait4expected(shell,"active connections found","No connection specified.")
#         wait4expected(shell,"Error","No Error is expected")
        

def test_oneCombination(server_shell,ssh_client,combinationIndex,csv_abspath,ipaddrs,ports):
    """
    The core function, to test, for a specific combination, the multicast traffic and write/append the results on the csv output file. 
    """
    pandas.DataFrame([[["",combinations[combinationIndex],""]]]).to_csv(csv_abspath,index=False,header=False,mode="a")
    pandas.DataFrame([["ip address","port","loss rate(in %)"]]).to_csv(csv_abspath,index=False,header=False,mode="a")
    for multicastip in ipaddrs:
        for port in ports:
            server="iperf -s -u -B "+multicastip+" -p "+port+" & sleep 4\n"
            server_shell.send(server)
            wait4response(server_shell)
            
            client="iperf -c "+multicastip+" -u -t3 -i1 -T999 -p "+port+"\n"
            ssh_client.exec_command(client)
            
#             result=wait4expected(server_shell,'%)','159')
            time.sleep(4)
            if server_shell.recv_ready():
                result=str(server_shell.recv(100000))
                print(result)
                print("\n\n")
                loss_rate=result[result.rfind("(")+1:result.rfind(")")-1]
            else:
                loss_rate="100"                

            pandas.DataFrame([[multicastip,port,loss_rate]]).to_csv(csv_abspath,index=False,header=False,mode="a")
            
def test_allCombinations0(server_shell,ssh_client,client_shell,csv_abspath,ipaddrs,ports):
    combinationIndex=0
    for ssid_s in [-1]:
        connect(server_shell,ssid_s)   
        for ssid_c in [-1]:
            connect(client_shell,ssid_c)
            test_oneCombination(server_shell,ssh_client,combinationIndex,csv_abspath,ipaddrs,ports)
            combinationIndex+=1


            
def test_allCombinations(server_shell,ssh_client,client_shell,csv_abspath,ipaddrs,ports):
    combinationIndex=0
    for ssid_s in [-1,ssid_2g,ssid_5g]:
        connect(server_shell,ssid_s)   
        for ssid_c in [-1,ssid_2g,ssid_5g]:
            connect(client_shell,ssid_c)
            test_oneCombination(server_shell,ssh_client,combinationIndex,csv_abspath,ipaddrs,ports)
            combinationIndex+=1

