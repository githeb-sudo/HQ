"""
testbed_cfg = {                         FUT testbed configuration. Python dictionary for testbed specific settings
    "default": {
        "reconnect_attempts": 10,       The number of reconnect attempts by the framework for a lost ssh connection
        "reconnect_sleep": 10,          Configures the duration between ssh reconnect attempts in seconds
    },
    "server": {                         Configuration for the RPI server
        "host": "192.168.2.36",          RPI server IP on management subnet. The example here is for **** devices.
        "username": "****",
        "password": "****",
        "rsa": {
            "key_path": "/home/****/.ssh/id_rsa",
            "key_pass": "****",
        },
        "curl": {                       Configuration for web hosted file transfer
            "host": "http://192.168.4.1/"
        },
        "mgmt_vlan": 1,                 VLAN 1 is the system VLAN for the FUT testbed
        "tb_role": "server",            RPI server role in the FUT testbed.
                                          The role is linked to the network switch configuration.
    },
    "dut": {                            Device under test. These entries are modified for each specific device model.
        "host": "192.168.2.1",         DUT management IP
        "mgmt_vlan": 4,                 VLAN of DUT management IP. Synced with "host".
        "mgmt_ip": "192.168.2.1",      DUT management IP. Synced with "host".
        "wan_ip": "192.168.2.1",     DUT WAN IP
        "CFG_FOLDER": "",  DUT configuration folder name. The name depends on each specific device model.
        "tb_role": "gw",                DUT role in the FUT testbed. The role is linked to the network switch
                                          configuration. "gw" indicates the device uplink is wired.
    },
    "ref": {                            Reference device. Model "****" is used as default.
        "host": "192.168.4.11",         REF management IP
        "mgmt_vlan": 4,                 VLAN of REF management IP. Synced with "host".
        "mgmt_ip": "192.168.4.11",      REF management IP. Synced with "host".
        "wan_ip": "192.168.200.11",     REF WAN IP
        "CFG_FOLDER": "****",  REF configuration folder name. This model is supported by default.
        "tb_role": "leaf1",             REF role in the FUT testbed. The role is linked to the network switch
                                          configuration. "leaf" indicates the device uplink is wireless.
    },
    "client": {                         RPI client
        "host": "192.168.4.13",         RPI client management IP
        "mgmt_vlan": 4,                 VLAN of RPI client management IP. Synced with "host".
        "mgmt_ip": "192.168.4.13",      RPI client management IP. Synced with "host".
        "wan_ip": "192.168.200.13",     RPI client WAN IP. If the entry is removed, a lease from the DHCP pool is used.
        "tb_role": "rpi1",              RPI client role in the FUT testbed.
                                          The role is linked to the network switch configuration.
    },
}
"""


testbed_cfg = {
    "default": {
        "reconnect_attempts": 3,
        "reconnect_sleep": 3,
    },
    "server": {
        "host": "192.168.200.1",
        "username": "****",
        "password": "****",
        "rsa": {
            "key_path": "/root/.ssh/id_rsa",
            "key_pass": "****",
        },
        "curl": {
            "host": "http://192.168.200.1:80/" #"http://192.168.200.1:8000/"
        },
        "mqtt_settings": {
            "hostname": "192.168.200.1",
            "port": "65002"
        },
        "mgmt_vlan": 200,
        "tb_role": "server",
    },
    "dut": {
        "host": "192.168.200.27",
        "mgmt_vlan": 200,
        "mgmt_ip": "192.168.200.27",
        "wan_ip": "192.168.200.27",
        "CFG_FOLDER": "SP5280",
        "tb_role": "gw",
    },
    
    "ref": {
        "host": "192.168.1.1",
        "mgmt_vlan": 4,
        "mgmt_ip": "192.168.1.1",
        "wan_ip": "10.64.11.121",
        "CFG_FOLDER": "SP5280",
        "tb_role": "ref",
    },
    "client": {
        "host": "192.168.1.216",
        "mgmt_vlan": 4,
        "mgmt_ip": "192.168.1.216",
        "wan_ip": "192.168.1.216",
        "CFG_FOLDER": "client",
        "tb_role": "rpi",
    },
}
