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
    # Creates (updates if exists) interfaces with parameters: if_name, if_type
    "nm2_enable_disable_iface_network": [
        {
            "if_name": "eth2",
            "if_type": "eth",
        },
        {
            "if_name": "eth1",
            "if_type": "eth",
        },        
        {
            "if_name": "wl0",
            "if_type": "vif",
        },
        {
            "if_name": "wl1",
            "if_type": "vif",
        },
    ],
    # Creates (updates if exists) interfaces with parameters: if_name, if_type, start_pool, end_pool
    "nm2_ovsdb_configure_interface_dhcpd": [
        {
            "end_pool": "10.10.10.50",
            "if_name": "eth2",
            "if_type": "eth",
            "start_pool": "10.10.10.20",
        },
        {
            "end_pool": "10.10.10.50",
            "if_name": "eth1",
            "if_type": "eth",
            "start_pool": "10.10.10.20",
        },
        {
            "end_pool": "10.10.10.50",
            "if_name": "wl0",
            "if_type": "vif",
            "start_pool": "10.10.10.20",
        },
        {
            "end_pool": "10.10.10.50",
            "if_name": "wl1",
            "if_type": "vif",
            "start_pool": "10.10.10.20",
        },
    ],
    # Creates IP_Port_Forward with parameters: src_ifname, src_port, dst_ipaddr, dst_port, protocol
    "nm2_ovsdb_ip_port_forward": [
        {
            "dst_ipaddr": "10.10.10.123",
            "dst_port": "8080",
            "protocol": "tcp",
            "src_ifname": "br-wan",
            "src_port": "8080",
        },
    ],
    # Creates (updates if exists) interfaces with parameters: if_name, if_type
    "nm2_ovsdb_remove_reinsert_iface": [
        {
            "if_name": "eth2",
            "if_type": "eth",
        },
        {
            "if_name": "eth1",
            "if_type": "eth",
        },
        {
            "if_name": "wl0",
            "if_type": "vif",
        },
        {
            "if_name": "wl1",
            "if_type": "vif",
        },
    ],
    # Creates vlan interfaces with parameters: if_name, if_type, iteration_count, vlan_start
    "nm2_rapid_multiple_insert_delete_iface": [
        {
            "if_name": "eth2",
            "if_type": "vlan",
            "iteration_count": 20,
            "vlan_start": 100,
        },
        {
            "if_name": "eth1",
            "if_type": "vlan",
            "iteration_count": 20,
            "vlan_start": 100,
        },
    ],
    # Creates vlan interfaces with parameters: if_name, if_type, iteration_count, vlan_start
    "nm2_rapid_multiple_insert_delete_ovsdb_row": [
        {
            "if_name": "eth2",
            "if_type": "vlan",
            "iteration_count": 20,
            "vlan_start": 100,
        },
        {
            "if_name": "eth1",
            "if_type": "vlan",
            "iteration_count": 20,
            "vlan_start": 100,
        },
    ],
    # Creates (updates if exists) interfaces with parameters: if_name, if_type, broadcast
    "nm2_set_broadcast": [
        {
            "broadcast": "10.10.10.255",
            "if_name": "eth2",
            "if_type": "eth",
        },
        {
            "broadcast": "10.10.10.255",
            "if_name": "eth1",
            "if_type": "eth",
        },
        {
            "broadcast": "10.10.10.255",
            "if_name": "wl0",
            "if_type": "vif",
        },
        {
            "broadcast": "10.10.10.255",
            "if_name": "wl1",
            "if_type": "vif",
        },
    ],
    # Creates (updates if exists) interfaces with parameters: if_name, if_type, primary_dns, secondary_dns
    "nm2_set_dns": [
        {
            "if_name": "wl0",
            "if_type": "vif",
            "primary_dns": "1.2.3.4",
            "secondary_dns": "4.5.6.7",
        },
        {
            "if_name": "wl1",
            "if_type": "vif",
            "primary_dns": "8.9.10.11",
            "secondary_dns": "12.13.14.15",
        },
        {
            "if_name": "eth2",
            "if_type": "eth",
            "primary_dns": "16.17.18.19",
            "secondary_dns": "20.21.22.23",
        },
        {
            "if_name": "eth1",
            "if_type": "eth",
            "primary_dns": "24.25.26.27",
            "secondary_dns": "27.28.29.30",
        },
    ],
    # Creates (updates if exists) interfaces with parameters: if_name, interface type, gateway
    "nm2_set_gateway": [
        {
            "gateway": "10.10.10.50",
            "if_name": "eth2",
            "if_type": "eth",
            "test_script_timeout": 30,
        },
        {
            "gateway": "10.10.10.50",
            "if_name": "eth1",
            "if_type": "eth",
            "test_script_timeout": 30,
        },
        {
            "gateway": "10.10.10.50",
            "if_name": "wl0",
            "if_type": "vif",
            "channel": 1,
            "ht_mode": "HT20",
            "interface": {
                "channel": 36,
                "enabled": "true",
                "ht_mode": "HT20",
                "hw_mode": "11n",
                "if_name": "wl1",
                "mode": "ap",
                "security": {
                    "encryption": "WPA-PSK",
                    "key": "FutTestPSK",
                },
                "ssid": "FutTestSSID",
                "vif_if_name": "home-ap-24",
                "vif_radio_idx": 2,
            },
            "test_script_timeout": 30,
        },
        {
            "gateway": "10.10.10.50",
            "if_name": "wl1",
            "if_type": "vif",
            "ht_mode": "HT20",
            "channel": 36,
            "interface": {
                "channel": 36,
                "enabled": "true",
                "ht_mode": "HT20",
                "hw_mode": "11ac",
                "if_name": "wl1",
                "mode": "ap",
                "security": {
                    "encryption": "WPA-PSK",
                    "key": "FutTestPSK",
                },
                "ssid": "FutTestSSID",
                "vif_if_name": "home-ap-l50",
                "vif_radio_idx": 3,
            },
            "test_script_timeout": 90,
        },
    ],
    # Creates (updates if exists) interfaces with parameters: if_name, if_type, inet_addr
    "nm2_set_inet_addr": [
        {
            "if_name": "wl0",
            "if_type": "vif",
            "inet_addr": "10.10.10.30",
        },
        {
            "if_name": "wl1",
            "if_type": "vif",
            "inet_addr": "10.10.10.30",
        },
        {
            "if_name": "eth2",
            "if_type": "eth",
            "inet_addr": "10.10.10.30",
        },
        {
            "if_name": "eth1",
            "if_type": "eth",
            "inet_addr": "10.10.10.30",
        },
    ],
    # Creates (updates if exists) interfaces with parameters: if_name, if_type, ip_assign_scheme, inet_addr
    "nm2_set_ip_assign_scheme": [
        {
            "if_name": "wl0",
            "if_type": "vif",
            "ip_assign_scheme": "static",
        },
        {
            "if_name": "wl1",
            "if_type": "vif",
            "ip_assign_scheme": "static",
        },
        {
            "if_name": "eth2",
            "if_type": "eth",
            "ip_assign_scheme": "dhcp",
        },
        {
            "if_name": "eth1",
            "if_type": "eth",
            "ip_assign_scheme": "dhcp",
        },
    ],
    # Creates (updates if exists) interfaces with parameters: if_name, if_type, mtu
    "nm2_set_mtu": [
        {
            "if_name": "eth2",
            "if_type": "eth",
            "mtu": 2000,
        },
        {
            "if_name": "eth1",
            "if_type": "eth",
            "mtu": 2000,
        },
        {
            "if_name": "wl0",
            "if_type": "vif",
            "mtu": 2000,
        },
        {
            "if_name": "wl1",
            "if_type": "vif",
            "mtu": 2000,
        },
    ],
    # Creates (updates if exists) interfaces with parameters: if_name, if_type, NAT
    "nm2_set_nat": [
        {
            "NAT": "true",
            "if_name": "eth2",
            "if_type": "eth",
        },
        {
            "NAT": "true",
            "if_name": "eth1",
            "if_type": "eth",
        },
        {
            "NAT": "true",
            "if_name": "wl0",
            "if_type": "vif",
        },
        {
            "NAT": "true",
            "if_name": "wl1",
            "if_type": "vif",
        },
    ],
    # Creates (updates if exists) interfaces with parameters: if_name, if_type, netmask
    "nm2_set_netmask": [
        {
            "if_name": "eth2",
            "if_type": "eth",
            "netmask": "255.255.0.0",
        },
        {
            "if_name": "eth1",
            "if_type": "eth",
            "netmask": "255.255.0.0",
        },
        {
            "if_name": "wl0",
            "if_type": "vif",
            "netmask": "255.255.0.0",
        },
        {
            "if_name": "wl1",
            "if_type": "vif",
            "netmask": "255.255.0.0",
        },
    ],
    # Creates (updates if exists) interfaces with parameters: parent_if_name, vlan_id
    "nm2_set_parent_ifname": [
        {
            "parent_ifname": "eth2",
            "vlan_id": 100,
        },
        {
            "parent_ifname": "eth1",
            "vlan_id": 100,
        },
        {
            "parent_ifname": "wl0",
            "vlan_id": 100,
        },
        {
            "parent_ifname": "wl1",
            "vlan_id": 100,
        },
    ],
    # "nm2_set_upnp_mode": [
    #     {
    #         "external_if": "br-wan",
    #         "internal_if": "eth1",
    #         "test_script_timeout": 30,
    #     },
    #     {
    #         "external_if": "br-wan",
    #         "internal_if": "eth2",
    #         "test_script_timeout": 30,
    #     },
    # ],
    # Creates (updates if exists) interfaces with parameters: parent_if_name, vlan_id, if_name
    "nm2_vlan_interface": [
        {
            "parent_ifname": "eth2",
            "vlan_id": 100,
        },
        {
            "parent_ifname": "eth3",
            "vlan_id": 100,
        },
        {
            "parent_ifname": "wl0",
            "vlan_id": 100,
        },
        {
            "parent_ifname": "wl1",
            "vlan_id": 100,
        },
    ],
}
