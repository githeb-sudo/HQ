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


log_title "LEDM subtest: LED on off"

log "Positive test cases - assert result is true"
log "  Turning LED on, test if on"
led_config_ovsdb on || raise "Failed to turn on LED"
check_led_gpio_state on || raise "unexpected off state"

log "  Turning LED off, test if off"
led_config_ovsdb off || raise "Failed to turn off LED"
check_led_gpio_state off || raise  "unexpected on state"

log "Negative test cases - assert result is false"
log "  Turning LED on, test if off"
led_config_ovsdb on || raise "Failed to turn on LED"
wait_for_function_exitcode 1 "check_led_gpio_state off" 1 || raise  "Unexpected pass"

log "  Turning LED off, test if on"
led_config_ovsdb off || raise "Failed to turn off LED"
wait_for_function_exitcode 1 "check_led_gpio_state on" 1 || raise  "Unexpected pass"

pass

