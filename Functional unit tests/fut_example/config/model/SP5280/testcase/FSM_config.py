test_cfg = {
    "fsm_configure_fsm_tables": [
        {
            "handler": "dev_dns",
            "plugin": "libfsm_dns.so",
            "tap_name_postfix": "tdns",
        },
        {
            "handler": "dev_http",
            "plugin": "libfsm_http.so",
            "tap_name_postfix": "thttp",
        },
        {
            "handler": "dev_ndp",
            "plugin": "libfsm_ndp.so",
            "tap_name_postfix": "tupnp",
        },
    ],
    "fsm_configure_openflow_rules": [
        {
            "action": "normal,output:3001",
            "rule": "udp,tp_dst=53",
            "token": "dev_flow_dns_out",
        },
        {
            "action": "normal,output:4001",
            "rule": "tcp,tcp_dst=80",
            "token": "dev_flow_http_out",
        },
        {
            "action": "output:5001",
            "rule": "udp,udp_dst=1900",
            "token": "dev_flow_upnp_out",
        },
    ],
    "fsm_connect_wifi_client_to_ap": [
        {
            "channel": 36,
            "ht_mode": "HT40",
        },
    ],
    "fsm_create_tap_interface": [
        {
            "of_port": 3001,
            "tap_name_postfix": "tdns",
        },
        {
            "of_port": 4001,
            "tap_name_postfix": "thttp",
        },
        {
            "of_port": 5001,
            "tap_name_postfix": "tupnp",
        },
    ],
    "fsm_configure_test_dns_plugin": [
        {
            "channel": 36,
            "ht_mode": "HT40",
            "plugin": "libfsm_dns.so",
            "plugin_web_cat": "libfsm_wcnull.so",
            "test_script_timeout": 600,
            "url_block": "google.com",
            "url_redirect": "1.2.3.4",
        },
    ],
    "fsm_configure_test_http_plugin": [
        {
            "channel": 36,
            "ht_mode": "HT40",
            "plugin": "libfsm_http.so",
            "user_agent": "fsm_http_user_agent",
        },
    ],
    "fsm_configure_test_ndp_plugin": [
        {
            "channel": 36,
            "ht_mode": "HT40",
            "plugin": "libfsm_ndp.so",
        },
    ],
    "fsm_configure_test_upnp_plugin": [
        {
            "channel": 36,
            "ht_mode": "HT40",
            "plugin": "libfsm_upnp.so",
            "upnp_deviceType": "urn:plume-test:device:test:1",
            "upnp_friendlyName": "FUT test device",
            "upnp_manufacturer": "FUT testing, Inc",
            "upnp_manufacturerURL": "https://www.fut.com",
            "upnp_modelDescription": "FUT UPnP service",
            "upnp_modelName": "FUT tester",
            "upnp_modelNumber": "1.0",
        },
    ],
    "fsm_configure_test_walleye_plugin": [
        {
            "plugin": "libfsm_walleye_dpi.so",
        },
    ],
}