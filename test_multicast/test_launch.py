from subprocess import call

#-------------------------------------------------------------------------------------------------------------------------
"""
This part is required for both the configurations below
A/ Install in all devices: iperf,nmcli, nmap,openssh_server, python, with pip (ipython,paramiko)
B/ Verify the existence of the these python libraries: os,sys,shlex,subprocess,paramiko,argparse,time,pandas
C/ Set the value of abspath2test
"""

abspath2test="/home/g573222/workspace/test_multicast/python/test_multicast_main.py"


#-------------------------------------------------------------------------------------------------------------------------

#-----------------------> For a more automated test, uncomment and use the second configuration

"""
With this configuration:

A/ manually connect the server and the client to both 2.4GHz and 5GHz wifi
B/ specify the values of the following parameters 

"""

call(["python",abspath2test,
"-settings_id=1",# 1 for using this configuration, any other int in the other case
"-CSV_filename=test.csv",
"-ipaddrs_range=[224.0.0.1,224.0.0.2]", #LAN multicast ip addr 224.0.0.x/8 
#"-ports_range=[0,1023]",# -ports parameter is optional. If not specified, it will be a random number between 0 and 1023.
"-client_ip=192.168.4.18",       
"-username_client=plume",
"-password_client=plume",
"-server_ip=192.168.4.1",
"-username_server=plume",
"-password_server=plume",
"-ssid_2g=Iheb_2.4ghz",
"-ssid_5g=Iheb_5ghz",
"-wifi_password=orangepark612"
])



#-------------------------------------------------------------------------------------------------------------------------
#-----------------------> when all available is the hardware address and accessing either of the raspberries, getting their ip addresses and manually connecting them to WIFIs is unpleasant.
"""
With this configuration:
    
A/ Specifie the values of the following parameters

"""

"""
call(["python",abspath2test,
"-settings_id=2",# n>1 for using this configuration, 1 in the other case
"-CSV_filename=test.csv",
"-ipaddrs_range=[224.0.0.1,224.0.0.2]", #LAN multicast ip addr 224.0.0.x/8 
#"-ports_range=[0,1023]",# -ports parameter is optional. If not specified, it will be a random number between 0 and 1023.  
"-server_mac=dc:a6:32:81:9d:87",
"-username_server=ihebserver",
"-password_server=iheeb",
"-client_mac=dc:a6:32:ba:a9:a6",
"-username_client=iheb",
"-password_client=iheeb0",
"-ssid_2g=Iheb_2.4ghz",
"-ssid_5g=Iheb_5ghz",
"-wifi_password=orangepark612"
])
"""
