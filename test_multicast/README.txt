Hey there
Welcome to test_multicast

The purpose of this test is to check the LAN Multicast with a non standard flow.

Open test_launch.py and follow the instructions to run it.
Test d’un trafic multicast à flux non standard


Input:
	ipaddrs_range, server_mac, username_server, password_server, client_mac,  username_client, password_client, ssid_2g, ssid_5g, wifi_password

Return:
	csv_file   : for each scenario of a combination (server[ethernet, 2.4GHz, 5GHz],client[ethernet, 2.4GHz, 5GHz]), a date record values are (a tested multicast ip@, a tested port, the loss rate)