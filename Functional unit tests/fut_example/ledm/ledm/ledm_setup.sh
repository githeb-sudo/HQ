#!/bin/sh
# Include basic environment config from default shell file and if any from FUT framework generated /tmp/fut_set_env.sh file
if [ -e "/tmp/fut-base/fut_set_env.sh" ]; then
    source /tmp/fut-base/fut_set_env.sh
else
    source /tmp/fut-base/shell/config/default_shell.sh
fi

source ${FUT_TOPDIR}/shell/lib/unit_lib.sh
source ${FUT_TOPDIR}/shell/lib/ledm_lib.sh
source ${LIB_OVERRIDE_FILE}

device_init
start_openswitch
start_specific_manager ledm

empty_ovsdb_table AW_Debug
set_manager_log LEDM TRACE

sleep 3

exit 0
