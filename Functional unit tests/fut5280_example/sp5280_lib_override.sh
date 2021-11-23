#!/bin/sh
# Include basic environment config from default shell file and if any from FUT framework generated /tmp/fut_set_env.sh file
if [ -e "/tmp/fut-base/fut_set_env.sh" ]; then
    source /tmp/fut-base/fut_set_env.sh
else
    source /tmp/fut-base/shell/config/default_shell.sh
fi
###############################################################################
##############################-----CM-----#####################################
###############################################################################
# DESCRIPTION:
#   Function manipulates DNS traffic for source IP by adding or removing
#   DROP rule. Traffic can be blocked or unblocked.
#   Raises exception if there are not enough arguments, invalid arguments,
#   traffic cannot be manipulated.
# INPUT PARAMETER(S):
#   $1  ip address to block or unblock (required)
#   $2  type of rule to add, supported block, unblock (required)
#   $3  sudo command (defaults to sudo) (optional)
# RETURNS:
#   0   On success.
#   See DESCRIPTION
# USAGE EXAMPLE(S):
#   address_dns_manipulation 192.168.200.10 block
#   address_dns_manipulation 192.168.200.10 unblock
###############################################################################
address_dns_manipulation()
{
    local iptables_chain="INPUT"
    local fn_name="sp5280_override_lib:address_dns_manipulation"
    NARGS_MIN=2
    NARGS_MAX=3
    [ $# -ge ${NARGS_MIN} ] && [ $# -le ${NARGS_MAX} ] ||
        raise "${fn_name} requires ${NARGS_MIN}-${NARGS_MAX} input arguments, $# given" -arg
    local ip_address=${1}
    local type=${2}
    local sudo_cmd=${3:-"sudo"}
    local retry_cnt=3

    [ -z "${1}" ] || [ -z "${2}" ] && raise "Empty input argument(s)" -l "${fn_name}" -arg

    log -deb "${fn_name} - Manipulate DNS traffic: ${type} ${ip_address}"

    
    local iptables_args_udp="${iptables_chain} -p udp --dport 53  -s ${ip_address} -j DROP"
    local iptables_args_udp_ssl="${iptables_chain} -p udp --dport 53  -s ${ip_address}  -j DROP"
    local iptables_args_tcp="${iptables_chain} -p tcp --dport 53  -s ${ip_address} -j DROP"
    local iptables_args_tcp_ssl="${iptables_chain} -p tcp --dport 53   -s ${ip_address} -j DROP"

    address_dns_check "${ip_address}" "${type}" && return 0
    if [ "${type}" == "block" ]; then
        local action_type='-I'
        local wait_exit_code=0
    elif [ "${type}" == "unblock" ]; then
        local action_type='-D'
        # Waiting exit code 1 for unblock in case there is more than one rules of block in iptables
        # It will delete all the rules, iptables will return exit code 1 in case non existing rule tries to be deleted
        local wait_exit_code=1
    else
        raise "FAIL: Invalid input argument type, given: ${type}, supported: block, unblock" -l "${fn_name}" -arg
    fi

    local cmd_udp="${sudo_cmd} ${iptables_cmd} ${action_type} ${iptables_args_udp}"
    local cmd_udp_ssl="${sudo_cmd} ${iptables_cmd} ${action_type} ${iptables_args_udp_ssl}"
    local cmd_tcp="${sudo_cmd} ${iptables_cmd} ${action_type} ${iptables_args_tcp}"
    local cmd_tcp_ssl="${sudo_cmd} ${iptables_cmd} ${action_type} ${iptables_args_tcp_ssl}"

    wait_for_function_exitcode "${wait_exit_code}" "${cmd_udp}" "${retry_cnt}" &&
        log -deb "${fn_name} - DNS traffic ${type}ed for ${ip_address}" ||
        raise "FAIL: Could not ${type} DNS traffic for ${ip_address}" -l "${fn_name}" -ds
    wait_for_function_exitcode "${wait_exit_code}" "${cmd_tcp}" "${retry_cnt}" &&
        log -deb "${fn_name} - DNS traffic ${type}ed for ${ip_address}" ||
        raise "FAIL: Could not ${type} DNS traffic for ${ip_address}" -l "${fn_name}" -ds
    wait_for_function_exitcode "${wait_exit_code}" "${cmd_udp_ssl}" "${retry_cnt}" &&
        log -deb "${fn_name} - DNS traffic ${type}ed for ${ip_address}" ||
        raise "FAIL: Could not ${type} DNS traffic for ${ip_address}" -l "${fn_name}" -ds
    wait_for_function_exitcode "${wait_exit_code}" "${cmd_tcp_ssl}" "${retry_cnt}" &&
        log -deb "${fn_name} - DNS traffic ${type}ed for ${ip_address}" ||
        raise "FAIL: Could not ${type} DNS traffic for ${ip_address}" -l "${fn_name}" -ds
    address_dns_check "${ip_address}" "${type}" &&
        log -deb "${fn_name} - Command ${cmd_udp} success" ||
        raise "FAIL: Command manipulating iptables incorrectly reported success, check system" -l "${fn_name}" -ds
}
###############################################################################
# DESCRIPTION:
#   Function waits for Cloud status in Manager table to become
#   as provided in parameter.
#   Cloud statuses are:
#       ACTIVE          device is connected to the Cloud.
#       BACKOFF         device could not connect to the Cloud, will retry.
#       CONNECTING      connecting to the Cloud in progress.
#       DISCONNECTED    device is disconnected from the Cloud.
#   Raises an exception on fail.
# INPUT PARAMETER(S):
#   $1  desired Cloud state (required)
# RETURNS:
#   None.
#   See DESCRIPTION.
# USAGE EXAMPLE(S):
#   wait_cloud_state ACTIVE
###############################################################################
wait_cloud_state()
{
    fn_name="sp5280_lib_override:wait_cloud_state"
    local NARGS=1
    [ $# -ne ${NARGS} ] &&
        raise "${fn_name} requires ${NARGS} input argument(s), $# given" -arg
    wait_for_cloud_status=$1
    
    
    wait_for_function_response 0 "${OVSH} u Manager target:='' " &&
        log -deb "Success to force Manager to check AWLAN_Node for a target" ||
        raise "FAIL to force Manager to check AWLAN_Node for a target"

    log -deb "$fn_name - Waiting for the FUT cloud status $wait_for_cloud_status"
    wait_for_function_response 0 "${OVSH} s Manager status -r | grep -q \"$wait_for_cloud_status\"" 120 &&
        log -deb "$fn_name - FUT cloud status is $wait_for_cloud_status" ||
        raise "FAIL: FUT cloud status is not $wait_for_cloud_status" -l "$fn_name" -ow
    print_tables Manager
}

###############################################################################
# DESCRIPTION:
#   Function checks if traffic is already blocked or unblocked for source IP.
# INPUT PARAMETER(S):
#   $1  ip address to be blocked or unblocked (required)
#   $2  type of rule to add, supported block, unblock (required)
#   $3  sudo command (defaults to sudo) (optional)
# RETURNS:
#   0   Traffic already blocked or unblocked.
#   1   Traffic not yet manipulated.
# USAGE EXAMPLE(S):
#   address_dns_check
###############################################################################
address_dns_check()
{
    fn_name="sp5280_lib_override:address_dns_check"
    NARGS_MIN=2
    NARGS_MAX=3
    [ $# -ge ${NARGS_MIN} ] && [ $# -le ${NARGS_MAX} ] ||
        raise "${fn_name} requires ${NARGS_MIN}-${NARGS_MAX} input arguments, $# given" -arg
    local iptables_chain="INPUT"
    local ip_address=${1}
    local type=${2}
    local sudo_cmd=${3:-"sudo"}

    if [ "$type" == 'block' ]; then
        exit_code=0
    else
        exit_code=1
    fi

    check_ec=$(${sudo_cmd} ${iptables_cmd} -C ${iptables_chain} -p udp --dport 53 -s "$ip_address"  -j DROP)
    if [ "$?" -eq "$exit_code" ]; then
        log -deb "$fn_name - DNS traffic already ${type}ed for address $ip_address"
        return 0
    else
        return 1
    fi
}
###############################################################################
# DESCRIPTION:
#   Function runs manager setup if any of the managers in provided
#   parameters crashed. Checks existance of PID for provided managers.
#   If not found run setup for the crashed manager.
# INPUT PARAMETER(S):
#   $@  crashed managers
# RETURNS:
#   0   On success.
#   1   Manager is not executable.
#   See DESCRIPTION.
# USAGE EXAMPLE(S):
#   run_setup_if_crashed wm
#   run_setup_if_crashed nm cm
###############################################################################
run_setup_if_crashed()
{
    fn_name="sp5280_lib_override:run_setup_if_crashed"
    restart_managers
    for manager in "$@"
    do
        manager_pid_file="${OPENSYNC_ROOTDIR}/bin/$manager"
        pid_of_manager=$(get_pid "$manager_pid_file")
        if [ -z "$pid_of_manager" ]; then
            log -deb "$fn_name - Manager $manager crashed. Executing module environment setup"
            eval "${manager}_setup_test_environment" &&
                log -deb "$fn_name - Test environment for $manager success" ||
                raise "FAIL: Test environment for $manager failed" -l "$fn_name" -tc
        fi
    done
}
###############################################################################
###############################################################################


check_kconfig_option()
{
    kconfig_option_name=${1}
    kconfig_option_value=${2}
    kconfig_path="${OPENSYNC_ROOTDIR}/etc/kconfig"


    if [ ${1} == "CONFIG_MANAGER_WANO" ]; then
        false
    elif ! [ -f "${kconfig_path}" ]; then
        raise "kconfig file is not present on ${kconfig_path}" -l "unit_lib:check_kconfig_option" -ds  
    else
        cat "${kconfig_path}" | grep -q "${kconfig_option_name}=${kconfig_option_value}"       
    fi

    return $?
}

connect_to_fut_cloud()
{
    fn_name="sp5280_lib_override:connect_to_fut_cloud"
    target=${1:-"piranhav2-01-pub.us-east-1.int.tau.dev-charter.net"}
    port=${2:-"443"}
    cert_dir=${3:-"$FUT_TOPDIR/shell/tools/device/files"}
    ca_fname=${4:-"fut_ca.pem"}
    inactivity_probe=30000

    # log -deb "$fn_name - Configure certificates, check if file exists"
    # test -f "$cert_dir/$ca_fname" ||
    #     raise "FAIL: File $cert_dir/$ca_fname not found" -l "$fn_name" -ds

    # update_ovsdb_entry SSL -u ca_cert "$cert_dir/$ca_fname"
    #     log -deb "$fn_name - SSL ca_cert set to $cert_dir/$ca_fname" ||
    #     raise "FAIL: SSL ca_cert not set to $cert_dir/$ca_fname" -l "$fn_name" -ds

    # # Remove redirector, to not interfere with the flow
    # update_ovsdb_entry AWLAN_Node -u redirector_addr ''
    #     log -deb "$fn_name - AWLAN_Node redirector_addr set to ''" ||
    #     raise "FAIL: AWLAN_Node::redirector_addr not set to ''" -l "$fn_name" -ds

    # # Remove manager_addr, to not interfere with the flow
    # update_ovsdb_entry AWLAN_Node -u manager_addr ''
    #     log -deb "$fn_name - AWLAN_Node manager_addr set to ''" ||
    #     raise "FAIL: AWLAN_Node::manager_addr not set to ''" -l "$fn_name" -ds

    # # Inactivity probe sets the timing of keepalive packets
    # update_ovsdb_entry Manager -u inactivity_probe $inactivity_probe &&
    #     log -deb "$fn_name - Manager inactivity_probe set to $inactivity_probe" ||
    #     raise "FAIL: Manager::inactivity_probe not set to $inactivity_probe" -l "$fn_name" -ds

    # # Minimize AWLAN_Node::min_backoff timer (8s is ovsdb-server retry timeout)
    # update_ovsdb_entry AWLAN_Node -u min_backoff "8" &&
    #     log -deb "$fn_name - AWLAN_Node min_backof set to 8" ||
    #     raise "FAIL: AWLAN_Node::min_backoff not set to 8" -l "$fn_name" -ds

    # # Minimize AWLAN_Node::max_backoff timer
    # update_ovsdb_entry AWLAN_Node -u max_backoff "9" &&
    #     log -deb "$fn_name - AWLAN_Node max_backof set to 9" ||
    #     raise "FAIL: AWLAN_Node::max_backoff not set to 9" -l "$fn_name" -ds

    # # Clear Manager::target before starting
    # update_ovsdb_entry Manager -u target ''
    #     log -deb "$fn_name - Manager target set to ''" ||
    #     raise "FAIL: Manager::target not set to ''" -l "$fn_name" -ds

    # # Wait for CM to settle
    # sleep 2

    # update_ovsdb_entry AWLAN_Node -u redirector_addr "ssl:redirectorv2-dev-tau-dualstack.plume.tech:443" &&
    #     log -deb "$fn_name - AWLAN_Node redirector_addr set to ssl:redirectorv2-dev-tau-dualstack.plume.tech:$port" ||
    #     raise "FAIL: AWLAN_Node::redirector_addr not set to ssl:redirectorv2-dev-tau-dualstack.plume.tech:$port" -l "$fn_name" -ds

    # # AWLAN_Node::manager_addr is the controller address, provided by redirector
    # update_ovsdb_entry AWLAN_Node -u manager_addr "ssl:$target:$port" &&
    #     log -deb "$fn_name - AWLAN_Node manager_addr set to ssl:$target:$port" ||
    #     raise "FAIL: AWLAN_Node::manager_addr not set to ssl:$target:$port" -l "$fn_name" -ds

    log -deb "$fn_name - Waiting for FUT cloud status to go to ACTIVE"
    wait_cloud_state ACTIVE &&
        log -deb "$fn_name - Manager::status is set to ACTIVE. Connected to FUT cloud." ||
        raise "FAIL: Manager::status is not ACTIVE. Not connected to FUT cloud." -l "$fn_name" -ds
}
###############################################################################
vif_clean()
{
    fn_name="sp5280_lib_override:vif_clean"
    VIF_CLEAN_TIMEOUT=60
    log -deb "$fn_name - Purging VIF"

    empty_ovsdb_table Wifi_VIF_Config ||
        raise "FAIL: Could not empty table Wifi_VIF_Config: empty_ovsdb_table" -l "$fn_name" -oe
    empty_ovsdb_table Wifi_VIF_State ||
        raise "FAIL: Could not empty table Wifi_VIF_Config: empty_ovsdb_table" -l "$fn_name" -oe

    wait_for_empty_ovsdb_table Wifi_VIF_State ${VIF_CLEAN_TIMEOUT} ||
        raise "FAIL: Could not empty table Wifi_VIF_State: wait_for_empty_ovsdb_table" -l "$fn_name" -ow
}

start_qca_hostapd()
{
    fn_name="sp5280_lib_override:start_qca_hostapd"
    log -deb "$fn_name - Starting qca-hostapd"
    /etc/init.d/hostapd start
    sleep 2
}

start_qca_wpa_supplicant()
{
    fn_name="sp5280_lib_override:start_qca_wpa_supplicant"
    log -deb "$fn_name - Starting qca-wpa-supplicant"
    sudo systemctl start wpa_supplicant
    sleep 2
}
############################################ INFORMATION SECTION - START ###############################################
#
#   SP5280 libraries overrides
#
############################################ INFORMATION SECTION - STOP ################################################

############################################ UNIT OVERRIDE SECTION - START #############################################
check_survey_report_log()
{
    fn_name="sp5280_lib_override:check_survey_report_log"
    local NARGS=4
    [ $# -ne ${NARGS} ] &&
        raise "${fn_name} requires ${NARGS} input argument(s), $# given" -arg
    sm_radio_type=$1
    sm_channel=$2
    sm_survey_type=$3
    sm_log_type=$4

    case $sm_log_type in
    *processing_survey*)
        log_msg="Checking logs for survey $sm_radio_type channel $sm_channel reporting processing survey"
        die_msg="No survey processing done on $sm_radio_type $sm_survey_type on channel $sm_channel"
        sm_log_test_pass_msg="Survey processing done on $sm_radio_type $sm_survey_type on channel $sm_channel"
        sm_log_grep="$LOGREAD | grep -i 'Processing $sm_radio_type' | grep -i '$sm_survey_type $sm_channel'"
        ;;
    *scheduled_scan*)
        log_msg="Checking logs for survey $sm_radio_type channel $sm_channel reporting scheduling survey"
        die_msg="No survey scheduling done on $sm_radio_type $sm_survey_type on channel $sm_channel"
        sm_log_test_pass_msg="Survey scheduling done on $sm_radio_type $sm_survey_type on channel $sm_channel"
        sm_log_grep="$LOGREAD | grep -i 'Scheduled $sm_radio_type $sm_survey_type $sm_channel scan'"
        ;;
    *fetched_survey*)
        log_msg="Checking logs for survey $sm_radio_type channel $sm_channel reporting fetched survey"
        die_msg="No survey fetching done on $sm_radio_type $sm_survey_type on channel $sm_channel"
        sm_log_test_pass_msg="Survey fetching done on $sm_radio_type $sm_survey_type on channel $sm_channel"
        sm_log_grep="$LOGREAD  | grep -i 'Fetched $sm_radio_type'| grep -i  '$sm_survey_type $sm_channel'"#survey, after radio_type if_name
        ;;
    *sending_survey_report*)
        log_msg="Checking logs for survey $sm_radio_type channel $sm_channel reporting sending survey"
        die_msg="No survey sending done on $sm_radio_type $sm_survey_type on channel $sm_channel"
        sm_log_test_pass_msg="Survey sending done on $sm_radio_type $sm_survey_type on channel $sm_channel"
        sm_log_grep="$LOGREAD | grep -i 'Sending $sm_radio_type' | grep -i '$sm_survey_type $sm_channel survey report'"
        ;;
    *)
        raise "FAIL: Incorrect log type provided" -l "$fn_name" -arg
        ;;
    esac

    log "$fn_name - $log_msg"
    wait_for_function_response 0 "${sm_log_grep}" &&
        log -deb "$fn_name - $sm_log_test_pass_msg" ||
        raise "FAIL: $die_msg" -l "$fn_name" -tc
}

inspect_survey_report()
{
    fn_name="sp5280_lib_override:inspect_survey_report"
    local NARGS=6
    [ $# -ne ${NARGS} ] &&
        raise "${fn_name} requires ${NARGS} input argument(s), $# given" -arg
    sm_radio_type=$1
    sm_channel=$2
    sm_survey_type=$3
    sm_reporting_interval=$4
    sm_sampling_interval=$5
    sm_report_type=$6
    sm_stats_type="survey"

    sm_channel_list="[\"set\",[$sm_channel]]"

    empty_ovsdb_table Wifi_Stats_Config ||
        raise "FAIL: Could not empty Wifi_Stats_Config: empty_ovsdb_table" -l "$fn_name" -oe

    insert_ws_config \
        "$sm_radio_type" \
        "$sm_channel_list" \
        "$sm_stats_type" \
        "$sm_survey_type" \
        "$sm_reporting_interval" \
        "$sm_sampling_interval" \
        "$sm_report_type"
    if [ $sm_radio_type == "5G" ]; then
        check_survey_report_log "$sm_radio_type" "$sm_channel" "$sm_survey_type" processing_survey
        check_survey_report_log "$sm_radio_type" "$sm_channel" "$sm_survey_type" scheduled_scan
       # check_survey_report_log "$sm_radio_type" "neighbor" "$sm_survey_type" fetched_survey
        check_survey_report_log "$sm_radio_type" "$sm_channel" "$sm_survey_type" sending_survey_report
  
    else
        check_survey_report_log "$sm_radio_type" "" "client" processing_survey
        # check_survey_report_log "$sm_radio_type" "$sm_channel" "$sm_survey_type" scheduled_scan
        check_survey_report_log "$sm_radio_type" "" "rssi" fetched_survey
        check_survey_report_log "$sm_radio_type" "" "client" sending_survey_report
    fi
    empty_ovsdb_table Wifi_Stats_Config ||
        raise "FAIL: Could not empty Wifi_Stats_Config: empty_ovsdb_table" -l "$fn_name" -oe

    return 0
}


get_managers_script()
{
    # echo "/etc/init.d/opensync"
    echo "/etc/init.d/restart_nocnxloss.sh"
}

stop_healthcheck()
{
    log -deb "Healthcheck service not present on system"
    return 0
}

device_init()
{
    restart_managers
    disable_watchdog
    return $?
}

stop_managers()
{    
    fn_name="sp5280_lib_override:stop_managers"
    log -deb "$fn_name - Stopping OpenSync managers"
    # MANAGER_SCRIPT=$(get_managers_script)
    # $MANAGER_SCRIPT stop ||
    #     raise "FAIL: Issue during OpenSync manager stop" -l "$fn_name" -ds
    # sleep 10
    # killall -s SIGKILL dm cm nm wm lm sm bm um om qm fsm fm vm nfm ledm wano sshm maptm cam
    # pkill -9 toad
    # /etc/init.d/opensync stop#

}
restart_managers()
{
    fn_name="sp5280_lib_override:restart_managers"
    log -deb "$fn_name - Restarting OpenSync managers"
    MANAGER_SCRIPT=$(get_managers_script restart)
    ret=$($MANAGER_SCRIPT)
    ec=$?
    log -deb "$fn_name - manager restart exit code ${ec}"
    sleep 30
    return 0
}

restart_brwan()
{
    fn_name="sp5280_lib_override:restart_brwan"
    log -deb "$fn_name - Restarting brwan iface"
    BRWAN_SCRIPT=$(get_restore_brwan_script)
    ret=$($BRWAN_SCRIPT)
    ec=$?
    log -deb "$fn_name - manager restart exit code ${ec}"
    # sleep 30
    return 0
}

disable_watchdog()
{
    fn_name="sp5280_lib_override:disable_watchdog"
    echo 'V' > /dev/watchdog
    log -deb "$fn_name watchdog successfully disabled"
}



interface_is_up()
{
    fn_name="sp5280_lib_override:interface_is_up"
    local NARGS=1
    [ $# -ne ${NARGS} ] &&
        raise "${fn_name} requires ${NARGS} input argument(s), $# given" -arg
    if_name=$1

    if  echo "$if_name" | grep -q "wl.\." ;then
        ifconfig $if_name | grep -q "$if_name"    
    elif  echo "$if_name" | grep -q "wl" ;then
        wl -i $if_name radio | grep -q "0x0000"  
    else 
        ifconfig "$if_name" 2>/dev/null | grep Metric | grep -q UP
    fi
    return $?
}


check_restore_management_access()
{
    local fn_name="sp5280_lib_override:check_restore_management_access"
    log -deb "$fn_name - Restore not implemented - skipping"
    return 0
}
# ip_port_forward()
# {
    # ovsh i IP_Port_Forward dst_ipaddr:="10.10.10.111" dst_port:="80" src_port:="80"  protocol:="tcp" src_ifname:="eth00"
    # iptables -t nat --list -v | tr -s ' ' / | grep '/DNAT/'
    # ovsh i IP_Port_Forward
    # despite the success of the insert into the table. It is not reflected in the iptables
    # fn_name="nm2_lib:ip_port_forward"
    # local NARGS=1
    # [ $# -ne ${NARGS} ] &&
    #     raise "${fn_name} requires ${NARGS} input argument(s), $# given" -arg
    # if_name=$1
    #iptables -t nat --list -v  | tr -s ' ' / | grep '/DNAT/' | grep -q "$if_name"
# }

# check_restore_management_access()
# {
#     fn_name="unit_lib:check_restore_management_access"
#     log -deb "$fn_name - Checking and restoring needed management access"
#     mng_iface=${MGMT_IFACE:-eth0}
#     interface_is_up "${mng_iface}"
#     if [ "$?" = 0 ]; then
#         log -deb "$fn_name - Interface ${mng_iface} is UP"
#     else
#         log -deb "$fn_name - Interface ${mng_iface} is DOWN, bringing it UP"
#         wait_for_function_response 0 "ifconfig ${mng_iface} up" "${MGMT_IFACE_UP_TIMEOUT}" &&
#             log -deb "$fn_name - Interface ${mng_iface} brought UP" ||
#             log -err "FAIL: Could not bring up interface ${mng_iface}" -l "$fn_name" -ds
#     fi

#     interface_is_up "${mng_iface}.4"
#     if [ "$?" = 0 ]; then
#         log -deb "$fn_name - Interface ${mng_iface}.4 is UP"
#     else
#         log -deb "$fn_name - Interface ${mng_iface}.4 is DOWN, bringing it UP"
#         ifconfig "${mng_iface}.4" up &&
#             log -deb "$fn_name - Interface ${mng_iface}.4 brought UP" ||
#             log -deb "$fn_name - Failed to bring up interface ${mng_iface}.4, checking udhcpc"
#     fi

#     eth_04_address=$(interface_ip_address "${mng_iface}.4")
#     if [ -z "$eth_04_address" ]; then
#         log -deb "$fn_name - Interface ${mng_iface}.4 has no address, setting udhcpc"
#         log -deb "$fn_name - Running force address renew for ${mng_iface}.4"
#         no_address=1
#         while [ "$no_address" = 1 ]; do
#             log -deb "$fn_name - Killing old ${mng_iface}.4 udhcpc pids"
#             dhcpcd_pids=$(pgrep -f "/sbin/udhcpc .* ${mng_iface}.4")
#             # shellcheck disable=SC2086
#             kill $dhcpcd_pids &&
#                 log -deb "$fn_name - ${mng_iface}.4 udhcpc pids killed" ||
#                 log -deb "$fn_name - No ${mng_iface}.4 udhcpc pid to kill"
#             log -deb "$fn_name - Starting udhcpc on ${mng_iface}.4"
#             /sbin/udhcpc -f -S -i "${mng_iface}.4" -C -o -O subnet &>/dev/null &
#             log -deb "$fn_name - Waiting for ${mng_iface}.4 address"
#             wait_for_function_response notempty "interface_ip_address ${mng_iface}.4" "${MGMT_CONN_TIMEOUT}" &&
#                 log -deb "$fn_name - ${mng_iface}.4 address valid" && break ||
#                 log -deb "$fn_name - Failed to set ${mng_iface}.4 address, repeating"
#         done
#     else
#         log -deb "$fn_name - Interface ${mng_iface}.4 address is $eth_04_address"
#     fi
# }
############################################ UNIT OVERRIDE SECTION - STOP ##############################################

check_channel_at_os_level()
{
    wm2_channel=$1
    wm2_vif_if_name=$2
    fn_name="sp5280_lib_override:check_channel_at_os_level"

    log -deb "$fn_name - Checking channel at OS"

    wait_for_function_response 0 "wl -i $wm2_vif_if_name status | grep -F \"Primary channel: $wm2_channel\""

    if [ $? = 0 ]; then
        log -deb "$fn_name - Channel is set to $wm2_channel at OS level"
        return 0
    fi
    wl -i $wm2_vif_if_name status
    raise "Channel is NOT set to $wm2_channel" -l "$fn_name" -tc
}

check_ht_mode_at_os_level()
{
    wm2_ht_mode=$1
    wm2_vif_if_name=$2
    fn_name="sp5280_lib_override:check_ht_mode_at_os_level"

    log -deb "$fn_name - Checking HT MODE at OS level"
    ht_mode=$(echo $wm2_ht_mode | cut -c 3-6)
    wait_for_function_response 0 "wl -i $wm2_vif_if_name status | grep -F ${ht_mode}MHz"

    if [ $? = 0 ]; then
        log -deb "$fn_name - HT MODE: $wm2_ht_mode is SET at OS level"
        return 0
    else
        wl -i $wm2_vif_if_name status
        raise "HT MODE: $wm2_ht_mode is NOT set at OS" -l "$fn_name" -tc
    fi

}

check_tx_power_at_os_level()
{
    wm2_tx_power=$1
    wm2_if_name=$2
    fn_name="sp5280_lib_override:check_tx_power_at_os_level"

    log -deb "$fn_name - Checking Tx-Power at OS level"

    wait_for_function_response 0 "wl -i $wm2_if_name txpwr1 | cut -d \",\" -f2 | grep -F $wm2_tx_power" &&
        log -deb "$fn_name - Tx-Power: $wm2_tx_power is set at OS level" ||
        (
            wl -i "$wm2_if_name status"
            return 1
        ) || raise "Tx-Power: $wm2_tx_power is NOT set at OS" -l "$fn_name" -tc
}

check_beacon_interval_at_os_level()
{
    wm2_bcn_int=$1
    wm2_vif_if_name=$2
    fn_name="sp5280_lib_override:check_beacon_interval_at_os_level"

    log -deb "$fn_name - Checking BEACON INTERVAL at OS level"

    wait_for_function_response 0 "wl -i $wm2_vif_if_name bi | grep -F $wm2_bcn_int"
    if [ $? = 0 ]; then
        log -deb "$fn_name - BEACON INTERVAL: $wm2_bcn_int is SET at OS level"
        return 0
    else
        wl -i $wm2_vif_if_name bi
        raise "BEACON INTERVAL: $wm2_bcn_int is NOT set at OS" -l "$fn_name" -tc
    fi

}



get_process_cmd()
{
    echo "ps"
}

check_radio_vif_state()
{
    vif_args_c=""
    vif_args_w=""
    radio_args=""
    replace="func_arg"
    fn_name="sp5280_lib_override:check_radio_vif_state"

    interface_is_up "$if_name"

    if [ "$?" -eq 0 ]; then
        log -deb "$fn_name - Interface $if_name is up"
    else
        log -deb "$fn_name - Interface $if_name is not up"
        return 1
    fi


    while [ -n "$1" ]; do
        option=$1
        shift
        case "$option" in
            -if_name)
                radio_args="$radio_args $replace if_name $1"
                shift
                ;;
            -vif_if_name)
                vif_args="$vif_args $replace if_name $1"
                wm2_vif_if_name=$1
                shift
                ;;
            -vif_radio_idx)
                vif_args="$vif_args $replace vif_radio_idx $1"
                shift
                ;;
            -ssid)
                vif_args="$vif_args $replace ssid $1"
                shift
                ;;
            -channel)
                radio_args="$radio_args $replace channel $1"
                vif_args="$vif_args $replace channel $1"
                shift
                ;;
            -ht_mode)
                radio_args="$radio_args $replace ht_mode $1"
                shift
                ;;
            -hw_mode)
                radio_args="$radio_args $replace hw_mode $1"
                shift
                ;;
            -mode)
                vif_args="$vif_args $replace mode $1"
                shift
                ;;
        esac
    done

    func_params=${radio_args//$replace/-w}

    check_ovsdb_entry Wifi_Radio_State $func_params &&
        log -deb "$fn_name - Wifi_Radio_State is valid for given configuration" ||
        (
            log -deb "$fn_name - VIF_State does not exist" &&
            return 1
        )

    func_params=${vif_args//$replace/-w}
    check_ovsdb_entry Wifi_VIF_State $func_params &&
        log -deb "$fn_name - Wifi_Radio_State is valid for given configuration" ||
        (
            log -deb "$fn_name - VIF_State does not exist" &&
            return 1
        )
}

test_ledm_led_config()
{
    fn_name="sp5280_lib_override:test_ledm_led_config"

    log -deb "$fn_name - Turning on LED solid mode"
    led_config_ovsdb on solid ||
        raise "led_config_ovsdb on solid" -l "$fn_name" -fc
    check_led_gpio_state on solid ||
        raise "check_led_gpio_state on solid" -l "$fn_name" -fc
    sleep 1

    log -deb "$fn_name - LED on mode easing"
    led_config_ovsdb on easing ||
        raise "led_config_ovsdb on easing " -l "$fn_name" -fc
    check_led_gpio_state on easing ||
        raise "check_led_gpio_state on easing " -l "$fn_name" -fc
    sleep 1


    log -deb "$fn_name - Turning off LED solid mode"
    led_config_ovsdb off solid ||
        raise "led_config_ovsdb off solid" -l "$fn_name" -fc
    check_led_gpio_state off solid ||
        raise "check_led_gpio_state off solid" -l "$fn_name" -fc
    sleep 1

    log -deb "$fn_name - LED off mode easing"
    led_config_ovsdb off easing ||
        raise "led_config_ovsdb off easing " -l "$fn_name" -fc
    check_led_gpio_state off easing ||
        raise "check_led_gpio_state off easing " -l "$fn_name" -fc
    sleep 1
}





led_config_ovsdb()
{
    fn_name="sp5280_lib_override:led_config_ovsdb"
    color=${1:-"on"}
    mode=${2:-"solid"}    

    case "$color" in
    "on")
        color='blue'
        ;;        
    "off")
        color='red'  
        ;;   
    *)
        log -deb "$fn_name - This configuration is not supported!"
        return 1
    esac

    # mode_effect=$(shuf -i 0-1 -n 1)
    # case "$mode_effect" in
    #     0)
    #     mode='solid'
    #     ;;
    #     1)
    #     mode='easing'
    #     ;;
    # esac    
    # if [  $mode == on ]; then
    #     color='blue'
    #     log -deb "$fn_name - $mode LED on"    
    # elif [ $mode == easing ]; then
    #     mode='easing'
    #     log -deb "$fn_name - $mode LED easing"    
    # fi

    ${OVSH} u AWLAN_Node led_config:='["map",[["color","'$color'"],["mode","'$mode'"]]]' ||
        raise "FAIL: Could not update AWLAN_Node table" -l "$fn_name" -ow
}

check_led_gpio_state()
{
    fn_name="sp5280_lib_override:check_led_gpio_state"
    color=${1:-"on"}
    mode=${2:-"solid"} 

    case "$color" in
    "on")
        color='blue'
        ;;        
    "off")
        color='red'  
        ;;   
    *)
        log -deb "$fn_name - This configuration is not supported!"
        return 1
    esac

    $( ${OVSH} s AWLAN_Node led_config| grep $color | grep -q $mode) 

}
