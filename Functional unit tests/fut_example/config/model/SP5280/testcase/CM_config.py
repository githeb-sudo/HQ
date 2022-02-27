test_cfg = {
    "cm2_ble_status_interface_down": [
        {},
    ],
    "cm2_ble_status_internet_block": [
        {
            "test_script_timeout": 120,
        },
    ],
    "cm2_cloud_down": [
        {
            "test_script_timeout": 120,
            "unreachable_cloud_counter": 4,
        },
    ],
    "cm2_dns_failure": [
        {
            "test_script_timeout": 120,
        },
    ],
    # "cm2_internet_lost": [
    #     {
    #         "test_script_timeout": 120,
    #         "unreachable_internet_counter": 4,
    #     },
    # ],
    # "cm2_link_lost": [
    #     {},
    # ],

    "cm2_ssl_check": [
        {},
    ],
    # "cm2_verify_gre_tunnel_dut_gw": [
    #     {
    #         "bhaul_psk": "PreSharedKey",
    #         "bhaul_ssid": "fut.bhaul",
    #         "gw_bhaul_vif_radio_idx": 1,
    #         "gw_radio_channel": 44,
    #         "gw_radio_ht_mode": "HT80",
    #         "gw_radio_hw_mode": "11ac",
    #         "test_script_timeout": 300,
    #     },
    # ],

}

