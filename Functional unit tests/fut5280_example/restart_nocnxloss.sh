#!/bin/sh /etc/rc.common


SERVICE_DAEMONIZE=0
SERVICE_WRITE_PID=0
SERVICE_USE_PID=0

NAME=managers
PIDCOUNT=0

PLUME_DIR=/usr/opensync
BIN_DIR=${PLUME_DIR}/bin
LIB_DIR=${PLUME_DIR}/lib
TOOLS_DIR=${PLUME_DIR}/tools

OVSH=$TOOLS_DIR/ovsh

OVS_RUN_DIR=/var/run/openvswitch
OVS_ETC_DIR=/tmp/etc/openvswitch
OVS_CERT_DIR=${OVS_RUN_DIR}/certs

PL_RUN_DIR=/var/run/opensync
PL_ETC_DIR=/tmp/etc/opensync
PL_CERT_DIR=${PL_RUN_DIR}/certs
PL_DEVICE_MODE_PATH=/tmp/opensync-mode.json

BR_HOME=BR_LAN
L2UF_PORT=BR_LAN.l2uf1
HOME_TAG='home--1'


export PATH=${TOOLS_DIR}:$PATH


###############################################################################
ovsdb_start() {
    if [ "$CONFIG_OVSDB_SERVER_FULL_CONTROL" != "y" ]; then
        return
    fi

    if [ ! -d ${OVS_RUN_DIR} ]; then
        mkdir -p ${OVS_RUN_DIR}
        mkdir -p ${OVS_CERT_DIR}
        cp ${PLUME_DIR}/certs/* ${OVS_CERT_DIR}/.
    fi

    if [ ! -d ${OVS_ETC_DIR} ]; then
        mkdir -p ${OVS_ETC_DIR}
        cp /usr/opensync/etc/conf.db.bck ${OVS_ETC_DIR}/conf.db
    fi

    echo "Starting OpenSync OVSDB management"
    # ovsdb-server start against non-persistent DB
    
    pi=$(cat ${OVS_RUN_DIR}/ovsdb-server.pid)
    start-stop-daemon -S -b -x /usr/sbin/ovsdb-server -- \
        --remote=punix:${OVS_RUN_DIR}/db.sock \
        --remote=db:Open_vSwitch,Open_vSwitch,manager_options \
        --private-key=db:Open_vSwitch,SSL,private_key \
        --certificate=db:Open_vSwitch,SSL,certificate \
        --ca-cert=db:Open_vSwitch,SSL,ca_cert \
        --pidfile=${OVS_RUN_DIR}/ovsdb-server.pid \
        --log-file=/dev/null \
        --unixctl=${OVS_RUN_DIR}/ovsdb-server.$pi.ctl \
        ${OVS_ETC_DIR}/conf.db
    ln -sf /var/run/db.sock /var/run/openvswitch/db.sock
    cp /usr/opensync/etc/conf.db.bck /tmp/etc/openvswitch/conf.db
}

ovsdb_stop() {
    if [ "$CONFIG_OVSDB_SERVER_FULL_CONTROL" != "y" ]; then
        return
    fi

    echo "Stopping OpenSync OVSDB management"

    # ovsdb-server
    killall -s SIGKILL ovsdb-server

    # remove pre-populated db conf.db from ramdisk
    if [ -d ${OVS_RUN_DIR} ]; then
        rm -r ${OVS_RUN_DIR}
    fi
    if [ -d ${OVS_ETC_DIR} ]; then
        rm -r ${OVS_ETC_DIR}
    fi
}

ovstable_cleanup() {

    # Update AWLAN_Node and Manager tables
    $OVSH u AWLAN_Node \
        manager_addr:="" \
        mqtt_headers::'["map",[]]' \
        mqtt_settings::'["map",[]]' \
        mqtt_topics::'["map",[]]' &> /dev/null
    $OVSH u Manager \
        target:="" \
        is_connected:="false" \
        status::'["map",[]]' &> /dev/null

    # Clear tables
    $OVSH d Wifi_Radio_Config &> /dev/null
    $OVSH d Wifi_Radio_State &> /dev/null
    $OVSH d Wifi_VIF_Config &> /dev/null
    $OVSH d Wifi_VIF_State &> /dev/null
    $OVSH d Wifi_Inet_Config &> /dev/null
    $OVSH d Wifi_Inet_State &> /dev/null
    $OVSH d Wifi_Associated_Clients &> /dev/null

    $OVSH d DHCP_leased_IP &> /dev/null
    $OVSH d OVS_MAC_Learning &> /dev/null
    $OVSH d Client_Nickname_Config &> /dev/null
    $OVSH d Wifi_Master_State &> /dev/null
    $OVSH d Wifi_Stats_Config &> /dev/null
    $OVSH d Wifi_VIF_Neighbors &> /dev/null
    $OVSH d Wifi_Route_State &> /dev/null
    $OVSH d Node_State &> /dev/null

    $OVSH d Band_Steering_Clients &> /dev/null
    $OVSH d Band_Steering_Config &> /dev/null

    $OVSH d Openflow_Config &> /dev/null
    $OVSH d Openflow_State &> /dev/null
    $OVSH d Openflow_Tag &> /dev/null
    $OVSH d Openflow_Tag_Group &> /dev/null

    $OVSH d FSM_Policy &> /dev/null
    $OVSH d Flow_Service_Manager_Config &> /dev/null

    $OVSH d FCM_Filter &> /dev/null
    $OVSH d FCM_Report_Config &> /dev/null
    $OVSH d FCM_Collector_Config &> /dev/null

    $OVSH d Wifi_Test_Config &> /dev/null
    $OVSH d Wifi_Test_State &> /dev/null
}

ovsbridge_cleanup() {
    if [ "$CONFIG_BRIDGE_NATIVE" == "y" ] ; then
        return
    fi

    # Remove GRE interfaces
    for gre in $(ovsh s Wifi_Inet_Config -r -w if_type==gre if_name); do
        ovs-vsctl del-port $BR_HOME $gre
        ip link del $gre
    done

    # Remove tap interfaces
    for tap in $(ovsh s Wifi_Inet_Config -r -w if_type==tap if_name); do
        ovs-vsctl del-port $BR_HOME $tap
    done

    if [ "$CONFIG_PLATFORM_IS_BCM" == "y" ] ; then
        ovs-vsctl del-port $BR_HOME $L2UF_PORT
    fi
}


process_start(){
    if [ "$CONTROL_HW_VENDOR_PROCESSES" == "y" ]; then
        echo "Starting nas"
        nas
        echo "Starting eapd"
        eapd
    fi
}

process_stop(){
    # Backhaul DHCP service
    [ -e "$CONFIG_OSN_DHCPD_PID_PATH" ] && {
        kill $(cat $CONFIG_OSN_DHCPD_PID_PATH)
        rm $CONFIG_OSN_DHCPD_PID_PATH
    }

    if [ "$CONTROL_HW_VENDOR_PROCESSES" == "y" ]; then
        echo "Stopping nas"
        killall nas
        echo "Stopping eapd"
        killall eapd
    fi


}
lan_eth_setup()
{
    i=1
    while [[ $i -le 4 ]]
    do
        ifconfig "eth$i" up
        ovs-vsctl add-port "$1" "eth$i"
        let i=i+1
    done
}

bcm_start() {
    if [ "$CONFIG_PLATFORM_IS_BCM" != "y" ] || [ "$CONFIG_BRIDGE_NATIVE" == "y" ]; then
        return
    fi

    echo "Starting BCM"

    # Wait until home bridge is up and running
    echo "Waiting for home bridge..."
    while true; do
        ovs-vsctl list bridge $BR_HOME > /dev/null && {
            break;
        }
        sleep 2
    done

    #Set the flag to restart the openvswitch
    OPENVSWITCH_STARTED=0

    # Wait until ovsdb is ready
    while ! ovsdb-client list-dbs > /dev/null 2>&1
    do
        #Start openvswitch if it is not already done
        if [ $OPENVSWITCH_STARTED -eq 0 ]; then
            /etc/init.d/openvswitch start
            OPENVSWITCH_STARTED=1
        fi
        sleep 1
        echo -n .
        
    done
    MAC_ETH0=$(mac_get eth0)                             
    MAC_ETH1=$(mac_get eth1)
    echo "Adding BR_LAN with MAC address $MAC_ETH1"      
    ovs-vsctl add-br BR_LAN                              
    ovs-vsctl set bridge BR_LAN other-config:hwaddr="$MAC_ETH1"  
    ovs-ofctl add-flow BR_LAN table=0,priority=50,dl_type=0x886c,actions=local
    ovs-vsctl set Bridge BR_LAN mcast_snooping_enable=true                                                                              
    # ovs-vsctl set Bridge BR_LAN other_config:mcast-snooping-disable-flood-unregistered=true
                                                                                            
                                                          
                                                            
    echo "Adding $L2UF_PORT port"                                                     
    ovs-vsctl add-port $BR_HOME $L2UF_PORT -- set interface $L2UF_PORT type=internal ofport_request=5000
    ovs-ofctl add-flow $BR_HOME table=0,priority=50,dl_type=0x886c,actions=LOCAL    
    ovs-ofctl add-flow $BR_HOME 'priority=190,dl_dst=01:00:00:00:00:00/01:00:00:00:00:00,dl_type=0x05ff,dl_type=0x05ff,actions=NORMAL,output:500'                                                                                                                                                                     
    ovs-ofctl add-flow $BR_HOME 'priority=160,dl_type=0x86dd,ipv6_dst=ff02::fb,udp6,udp_dst=5353,actions=flood'
                                                                                                            
    ifconfig $L2UF_PORT up                                                                                  
                                                                                                            
    # Configure LAN ethernet                                                                                
    lan_eth_setup BR_LAN                                                                                    
                                                                                                            
    # Configure WAN interface                                                                               
    ethswctl -c wan -i eth0 -o enable                                                                       
    ip link set dev eth0 up

    echo "Adding br-wan with MAC address $MAC_ETH0"                           
    ovs-vsctl add-br br-wan                                                                   
    ovs-vsctl set bridge br-wan other-config:hwaddr="$MAC_ETH0"                               
    ovs-vsctl set int br-wan mtu_request=1500                                                
    ovs-vsctl add-port br-wan eth0  
    /sbin/udhcpc -i br-wan -r 192.168.200.27

    # Configure ARPs                                                                                        
    echo 1 | tee /proc/sys/net/ipv4/conf/*/arp_ignore
    ovsdb-client transact '                                                                                 
    ["Open_vSwitch", {                                                                                      
        "op": "update",                                                                                     
        "table": "Open_vSwitch",                                                                            
        "where": [],                                                                                        
        "row": {                                                                                            
            "other_config": ["map", [["stats-update-interval", "3600000"] ]]                                
        }                                                                                                   
    }]' 
    # Create Openflow_Tag entry for home tag. This is needed because originally this is created by cloud and populated by wm.
    # In case that there is no cloud connection entry for home tag will not be created and wm will skip adding client to it.
    # This hp rules uses those tag so we need to create an entry so it is available even without cloud.
    $OVSH i Openflow_Tag name:=$HOME_TAG
    $OVSH i Openflow_Config action:="normal,in_port" bridge:=$BR_HOME priority:=1 rule:='in_port=${hp_ports},dl_dst=$['$HOME_TAG']' table:=0 token:=dev_hp_g_clients
    $OVSH i Openflow_Config action:="normal,in_port" bridge:=$BR_HOME priority:=1 rule:='in_port=${hp_ports},dl_dst=01:00:00:00:00:00/01:00:00:00:00:00' table:=0 token:=dev_hp_t_mbcast

    echo "Starting BCM: OK"
}

bcm_stop() {
    if [ "$CONFIG_PLATFORM_IS_BCM" != "y" ] ; then
        return
    fi

    echo "Stopping BCM"

    # Down the wifi interfaces
    for iface in $(ovsh s Wifi_VIF_Config -r if_name); do

        case "$iface" in
            *wl* )
            echo "Down: $iface"
            wlctl -i $iface bss down > /dev/null 2>&1
            wlctl -i $iface ssid "" > /dev/null 2>&1
            wlctl -i $iface macmode 0 > /dev/null 2>&1
            wlctl -i $iface mac none > /dev/null 2>&1
        esac

    done

    echo "Stopping BCM: OK"
}


sys_start() {
    # Generic sys start

    # BCM specific sys start
    bcm_start

    # other process start
    process_start
}

sys_cleanup() {
    # Generic sys cleanup

    # BCM specific sys stop
    bcm_stop

    # other process stop
    process_stop
}

managers_start() {
    if [ ! -d ${PL_RUN_DIR} ]; then
        mkdir -p ${PL_RUN_DIR}
        mkdir -p ${PL_CERT_DIR}
        cp ${PLUME_DIR}/certs/* ${PL_CERT_DIR}/.
    fi

    echo "Starting OpenSync managers"
    start-stop-daemon -S -b -x ${BIN_DIR}/dm

    echo "Starting OpenSync managers: OK"
    $OVSH i Openflow_Config action:="resubmit(,4)" bridge:=BR_LAN priority:=13 rule:="dl_type=0x888e" table:=0 token:="dev_sys_t_eapol"
    $OVSH i Openflow_Config action:="local" bridge:=BR_LAN priority:=14 rule:='dl_type=0x888e,dl_dst=${service_ap_macs}' table:=0 token:="dev_sys_t_pae_eapol"

}

managers_stop() {
    # Get manager list based on kconfig defines
    CFG_MANAGERS="dm wm nm cm sm lm qm bm om fsm pm fcm"

    echo "Stopping OpenSync managers"
    killall -s SIGKILL $CFG_MANAGERS > /dev/null 2>&1

    # Cleanup
    if [ -d ${PL_RUN_DIR} ]; then
        rm -r ${PL_RUN_DIR}
    fi

    echo "Stopping OpenSync managers: OK"
}

start() {
    # Start ovsdb-server
    ovsdb_start


    # Start/initialize system
    sys_start

    # Start OpenSync managers
    managers_start
}

stop() {
    # Stop OpenSync managers
    managers_stop

    # System cleanup
    sys_cleanup

    # Stop ovs related stuff
    ovsbridge_cleanup
    ovstable_cleanup
    ovsdb_stop

    if [ "$CONFIG_STOP_SAGEMCOM_EXCHANGE_MANAGER" == "y" ]; then
        # Stop connector to repopulate the tables
        killall -s SIGKILL xm &> /dev/null
    fi
    # /etc/init.d/hostap stop
    sleep 10
}

restart() {
    stop
    start
    sleep 5
    dropbear
    iptables -A INPUT -j ACCEPT
    sleep 5
    $OVSH u Wifi_VIF_Config enabled:=false
    sleep 5
    $OVSH u Wifi_VIF_Config enabled:=true

}

