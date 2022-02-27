test_cfg = {
    "nm2_configure_nonexistent_iface": [
        {
            "if_name": "test1",
            "if_type": "eth",
            "inet_addr": "10.10.10.15",
        },
        {
            "if_name": "test2",
            "if_type": "vif",
            "inet_addr": "10.10.10.16",
        },
        {
            "if_name": "test3",
            "if_type": "bridge",
            "inet_addr": "10.10.10.17",
        },
        {
            "if_name": "test4",
            "if_type": "tap",
            "inet_addr": "10.10.10.18",
        },
    ],
    "nm2_enable_disable_iface_network": [
        {
            "if_name": "eth3",
            "if_type": "eth",
        },
        {
            "if_name": "wifi0",
            "if_type": "vif",
        },
        {
            "if_name": "wifi1",
            "if_type": "vif",
        },
    ],
    "nm2_ovsdb_configure_interface_dhcpd": [
        {
            "end_pool": "10.10.10.50",
            "if_name": "eth3",
            "if_type": "eth",
            "start_pool": "10.10.10.20",
        },
        {
            "end_pool": "10.10.10.50",
            "if_name": "wifi0",
            "if_type": "vif",
            "interface": {
                "channel": 11,
                "enabled": "true",
                "ht_mode": "HT20",
                "hw_mode": "11n",
                "if_name": "wifi0",
                "mode": "ap",
                "security": {
                    "encryption": "WPA-PSK",
                    "key": "FutTestPSK",
                },
                "ssid": "FutTestSSID",
                "vif_if_name": "home-ap-24",
                "vif_radio_idx": 2,
            },
            "start_pool": "10.10.10.20",
        },        
        # {
        #     "channel": 2,
        #     "end_pool": "10.10.10.50",
        #     "ht_mode": "HT20",
        #     "if_name": "wifi1",
        #     "if_type": "vif",
        #     "start_pool": "10.10.10.20",
        # },
        # {
        #     "channel": 36,
        #     "end_pool": "10.10.10.50",
        #     "ht_mode": "HT40",
        #     "if_name": "wifi0",
        #     "if_type": "vif",
        #     "start_pool": "10.10.10.20",
        # },
    ],
    "nm2_ovsdb_ip_port_forward": [
        {
            "dst_ipaddr": "10.10.10.123",
            "dst_port": "80",
            "protocol": "tcp",
            "src_ifname": "BR_LAN",
            "src_port": "8080",
        },
        # {
        #     "dst_ipaddr": "10.10.10.123",
        #     "dst_port": "80",
        #     "protocol": "tcp",
        #     "src_ifname": "BR_DATA",
        #     "src_port": "8080",
        # },
        {
            "dst_ipaddr": "10.10.10.123",
            "dst_port": "80",
            "protocol": "tcp",
            "src_ifname": "eth3",
            "src_port": "8080",
        },
        {
            "dst_ipaddr": "10.10.10.123",
            "dst_port": "80",
            "protocol": "tcp",
            "src_ifname": "wifi0",
            "src_port": "8080",
        },
        {
            "dst_ipaddr": "10.10.10.123",
            "dst_port": "80",
            "protocol": "tcp",
            "src_ifname": "wifi1",
            "src_port": "8080",
        },
    ],
    "nm2_ovsdb_remove_reinsert_iface": [
        {
            "if_name": "eth3",
            "if_type": "eth",
        },
        {
            "if_name": "wifi1",
            "if_type": "vif",
        },
        {
            "if_name": "wifi0",
            "if_type": "vif",
        },
        {
            "if_name": "wifi1.1",
            "if_type": "vif",
        },
        {
            "if_name": "wifi0.1",
            "if_type": "vif",
        },
        {
            "if_name": "wifi1.2",
            "if_type": "vif",
        },
        {
            "if_name": "wifi0.2",
            "if_type": "vif",
        },
        {
            "if_name": "wifi1.3",
            "if_type": "vif",
        },
        {
            "if_name": "wifi0.3",
            "if_type": "vif",
        },
    ],
    "nm2_set_broadcast": [
        {
            "broadcast": "10.10.10.255",
            "if_name": "eth3",
            "if_type": "eth",
        },
        {
            "broadcast": "10.10.10.255",
            "if_name": "wifi1",
            "if_type": "vif",
        },
        {
            "broadcast": "10.10.10.255",
            "if_name": "wifi0",
            "if_type": "vif",
        },
    ],
    "nm2_set_dns": [
        {
            "if_name": "wifi1",
            "if_type": "vif",
            "primary_dns": "1.2.3.4",
            "secondary_dns": "4.5.6.7",
        },
        {
            "if_name": "wifi0",
            "if_type": "vif",
            "primary_dns": "8.9.10.11",
            "secondary_dns": "12.13.14.15",
        },
        {
            "if_name": "eth3",
            "if_type": "eth",
            "primary_dns": "16.17.18.19",
            "secondary_dns": "20.21.22.23",
        },
    ],
    "nm2_set_gateway": [
        {
            "gateway": "10.10.10.50",
            "if_name": "BR_DATA",
            "if_type": "eth",
        },
        {
            "channel": 2,
            "gateway": "10.10.10.50",
            "ht_mode": "HT20",
            "if_name": "wifi1.2",
            "if_type": "vif",
        },
        {
            "channel": 36,
            "gateway": "10.10.10.50",
            "ht_mode": "HT20",
            "if_name": "wifi0.2",
            "if_type": "vif",
        },
    ],
    "nm2_set_inet_addr": [
        {
            "if_name": "wifi1",
            "if_type": "vif",
            "inet_addr": "10.10.10.30",
        },
        {
            "if_name": "wifi0",
            "if_type": "vif",
            "inet_addr": "10.10.10.30",
        },
        {
            "if_name": "eth3",
            "if_type": "eth",
            "inet_addr": "10.10.10.30",
        },
    ],
    "nm2_set_ip_assign_scheme": [
        {
            "if_name": "wifi1",
            "if_type": "vif",
            "ip_assign_scheme": "static",
        },
        {
            "if_name": "wifi0",
            "if_type": "vif",
            "ip_assign_scheme": "static",
        },
        {
            "if_name": "eth3",
            "if_type": "eth",
            "ip_assign_scheme": "dhcp",
        },
    ],
    "nm2_set_mtu": [
        {
            "if_name": "eth3",
            "if_type": "eth",
            "mtu": 1400,
        },
        {
            "if_name": "eth3",
            "if_type": "eth",
            "mtu": 1500,
        },
        {
            "if_name": "wifi1",
            "if_type": "vif",
            "mtu": 1500,
        },
        {
            "if_name": "wifi1",
            "if_type": "vif",
            "mtu": 2000,
        },
        {
            "if_name": "wifi0",
            "if_type": "vif",
            "mtu": 1500,
        },
        {
            "if_name": "wifi0",
            "if_type": "vif",
            "mtu": 2000,
        },
    ],
    "nm2_set_nat": [
        {
            "NAT": "true",
            "if_name": "eth3",
            "if_type": "eth",
        },
        {
            "NAT": "true",
            "if_name": "wifi1",
            "if_type": "vif",
        },
        {
            "NAT": "true",
            "if_name": "wifi0",
            "if_type": "vif",
        },
    ],
    "nm2_set_netmask": [
        {
            "if_name": "eth3",
            "if_type": "eth",
            "netmask": "255.255.0.0",
        },
        {
            "if_name": "wifi1",
            "if_type": "vif",
            "netmask": "255.255.0.0",
        },
        {
            "if_name": "wifi0",
            "if_type": "vif",
            "netmask": "255.255.0.0",
        },
    ],
}
