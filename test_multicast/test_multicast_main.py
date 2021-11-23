import os,sys,shlex,subprocess,paramiko,argparse,time,pandas
from numpy.random import randint
import numpy as np
from socket import timeout

from test_multicast_util import *


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
parameters=namespace.__dict__
locals().update(parameters)

parameters.pop('ports_range',"")
check_all(parameters)

abspath=sys.argv[0]
csv_abspath=abspath[:abspath.rfind("/")+1]+CSV_filename
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





server_shell =ssh_server.invoke_shell()
time.sleep(1)
wait4response(server_shell)


client_shell =ssh_client.invoke_shell()
time.sleep(1)
wait4response(client_shell)


shellnWifi_prepare(client_shell,password_client,settings_id,ssid_2g,ssid_5g,wifi_password)   
shellnWifi_prepare(server_shell,password_server,settings_id,ssid_2g,ssid_5g,wifi_password)


test_allCombinations(server_shell,ssh_client,client_shell,csv_abspath,ipaddrs,ports)

ssh_server.close()
ssh_client.close()
