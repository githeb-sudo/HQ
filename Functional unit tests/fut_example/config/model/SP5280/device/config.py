"""
    Configuration 'framework_cfg' determines variables used within the framework.

    'device_version_cmd' - Command that retrieves the FW version from the device (string)(required)
    'log_dump_path' - Path relative to FUT sources on testbed server, where log tarballs are placed (string)(legacy)
    'log_messages_path' - Path relative to FUT sources on testbed server, where system logs are placed (string)(legacy)
    'password' - Password for device management SSH access  (string)(optional, if using ssh key)
    'pod_api_model': - Determine which lib_testbed library to use for device access (string)
    'py_test_timeout' - Timeout in seconds for each pytest testcase (integer)(required)
    'test_script_timeout' - Timeout in seconds, used to determine shell timeouts (integer)(required)
    'transfer_method' - File transfer method to and from the device (string)(required, options: 'curl', 'scp'=default)
    'username' - Username for device management SSH access (string)(required)
"""

framework_cfg = {
    'device_version_cmd': "sed -n 11p /etc/issue | awk '{print $3}' | sed 's/(//g' | sed 's/)//g'",#"uname -r",
    'log_dump_path': 'logpull/',
    'log_messages_path': 'logread/',
    'username': '*****',
    'password': '****',
    'pod_api_model': 'SP5280',
    'py_test_timeout': 30,
    'test_script_timeout': 30,
    'transfer_method': 'scp',  
}

"""
    Configuration 'shell_cfg' determines the environment variables exported on the device for shell script execution.

    Configuration values of type tuple are constructed during runtime, by replacing curly braces in the first item with
    values of the variables in subsequent items. For example, the 'OVSH' key will evaluate into the value:
        'OVSH': '/usr/opensync/tools/ovsh --quiet --timeout=30000'
    if the variables have values: opensync_rootdir = '/usr/opensync' and test_script_timeout = 30

    'DEFAULT_WAIT_TIME' - Timeout in milliseconds used for ovsh commands
    'FUT_TOPDIR' - Top directory of FUT on the device
    'LIB_OVERRIDE_FILE' - path to the library override file on the device. This file is used to override default
        implementation of functions in FUT libraries, to match device execution environment and capabilities.
    'LOGDUMP' (optional) command which outputs a tarball containing system logs into /tmp/manual_logpull.tar.gz
    'LOGREAD' - Command for reading system logs
    'MODEL' - Model string as reported by OpenSync
    'OPENSYNC_ROOTDIR' - Root directory of OpenSync on the device
    'OVSH' - 'ovsh' tool invocation command, containing absolute path to the tool and all desired flags
    'PATH' - Export a custom system PATH on the device and override the default system PATH
    'MGMT_IFACE' - Interface name for management access
"""





shell_cfg = {
    'DEFAULT_WAIT_TIME': ('{}', 'test_script_timeout'),
    'FUT_TOPDIR': '/tmp/fut-base',
    'ifconfig': '/sbin/ifconfig',
    'LIB_OVERRIDE_FILE': ('{}/shell/lib/override/sp5280_lib_override.sh', 'fut_dir'),
    'LOGDUMP': ('{}/bin/lm_logs_collector.sh --stdout', 'opensync_rootdir'),
    'LOGREAD': ('{}/tools/logread', 'opensync_rootdir'),
    'MODEL': 'SP5280',
    'OPENSYNC_ROOTDIR': '/usr/opensync',
    'OVSH': ('{}/tools/ovsh --quiet --timeout={}000', 'opensync_rootdir', 'test_script_timeout'),
    'PATH': ('/bin:/sbin:/usr/bin:/usr/sbin:{}/tools:/bin/sh', 'opensync_rootdir'),
    'MGMT_IFACE': 'br-wan',
}



device_cfg = {
    'backhaul_ap': {
        '24g': 'wl1.1',
        '5g': 'wl0.1',
        '5gl': None,
        '5gu': None,
    },
    'backhaul_sta': {
        '24g': 'wl1.0',
        '5g': 'wl0.0',
        '5gl': None,
        '5gu': None,
    },
    'cert_dir_path': '/var/certs/',
    'device_type': 'extender',
    'home_ap': {
        '24g': 'wl1.2',
        '5g': 'wl0.2',
        '5gl': None,
        '5gu': None,
    },
    'interface_name_eth_lan': 'BR_LAN',
    'interface_name_eth_wan': 'eth0',
    'interface_name_lan_bridge': 'br-wan',
    'interface_name_ppp_wan': 'br-wan',
    'interface_name_wan_bridge': 'br-wan',
    'model_string': 'SAC2V1S',
    'mtu_backhaul': 1552,
    'mtu_uplink_gre': 1514,
    'mtu_wan': 1500,
    'onboard_ap': {
        '24g': 'wl0.3',
        '5g': 'wl1.3',
        '5gl': None,
        '5gu': None,
    },
    'patch_port_lan-to-wan': 'patch-h2w',
    'patch_port_wan-to-lan': 'patch-w2h',
    'phy_radio_name': {
        '24g': 'wl1',
        '5g': 'wl0',
        '5gl': None,
        '5gu': None,
    },
    'radio_antennas': {
        '24g': '4x4', 
        '5g': '4x4',
        '5gl': None,
        '5gu': None,
    },
    'radio_channels': {
        '24g': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11],
        '5g': [36, 40, 44, 48, 52, 56, 60, 64, 100, 104, 108, 112, 116, 120, 124, 128, 132, 136, 140, 144, 149, 153, 157, 161, 165],
        '5gl': None,
        '5gu': None,
    },
    'regulatory_domain': "US",
    'um_fw_download_path': '/tmp/pfirmware/',
    'uplink_gre': {
        '24g': 'g-wl1',
        '5g': 'g-wl0',
        '5gl': None,
        '5gu': None,
    },
    'vif_radio_idx': {
        'backhaul_ap': 1,
        'backhaul_sta': 0,
        'home_ap': 2,
        'onboard_ap': 3,
    },
}
