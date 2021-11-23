test_cfg = {
    # "onbrd_verify_bridge_mode": [
    #     {},
    # ],
    # "onbrd_verify_router_mode": [
    #     {
    #         "dhcp_end_pool": "10.10.10.50",
    #         "dhcp_start_pool": "10.10.10.20",
    #     },
    # ],    
    "onbrd_verify_client_certificate_files": [
        {
            "cert_file": "ca_cert",
        },
        {
            "cert_file": "certificate",
        },
        {
            "cert_file": "private_key",
        },
    ],
    # "onbrd_verify_client_tls_connection": [
    #     {
    #         "test_script_timeout": 120,
    #         "tls_ver": "1.0",
    #     },
    #     {
    #         "test_script_timeout": 120,
    #         "tls_ver": "1.1",
    #     },
    #     {
    #         "test_script_timeout": 120,
    #         "tls_ver": "1.2",
    #     },
    # ],
    "onbrd_verify_device_mode_awlan_node": [
        {
            "device_mode": "not_set",
        },
    ],
    "onbrd_verify_dhcp_dry_run_success": [
        {
            "if_name": "eth1",
        },
    ],
    "onbrd_verify_dut_system_time_accuracy": [
        {
            "time_accuracy": "2",
        },
    ],
    "onbrd_verify_fw_version_awlan_node": [
        {
            "search_rule": "pattern_match",
        },
    ],
    "onbrd_verify_home_vaps_on_home_bridge": [
        {
            "channel": 2,
            "ht_mode": "HT20",
            "radio_band": "24g",
        },
        {
            "channel": 40,
            "ht_mode": "HT20",
            "radio_band": "5g",
        },
    ],
    "onbrd_verify_home_vaps_on_radios": [
        {
            "channel": 2,
            "ht_mode": "HT20",
            "radio_band": "24g",
        },
        {
            "channel": 40,
            "ht_mode": "HT20",
            "radio_band": "5g",
        },
    ],
    "onbrd_verify_id_awlan_node": [
        {},
    ],
    "onbrd_verify_manager_hostname_resolved": [
        {
            "test_script_timeout": 120,
        },
    ],
    "onbrd_verify_model_awlan_node": [
        {},
    ],
    "onbrd_verify_number_of_radios": [
        {},
    ],
    "onbrd_verify_onbrd_vaps_on_radios": [
        {
            "channel": 2,
            "ht_mode": "HT20",
            "radio_band": "24g",
        },
        {
            "channel": 40,
            "ht_mode": "HT40",
            "radio_band": "5g",
        },
    ],
    "onbrd_verify_redirector_address_awlan_node": [
        {},
    ],

    "onbrd_verify_wan_ip_address": [
        {},
    ],
}
