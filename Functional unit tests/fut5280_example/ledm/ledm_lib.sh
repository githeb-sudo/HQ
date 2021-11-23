#!/bin/sh
# Include basic environment config
if [ -e "/tmp/fut-base/fut_set_env.sh" ]; then
    source /tmp/fut-base/fut_set_env.sh
else
    source ${FUT_TOPDIR}/shell/config/default_shell.sh
fi
source ${FUT_TOPDIR}/shell/lib/unit_lib.sh
source ${LIB_OVERRIDE_FILE}

############################################ INFORMATION SECTION - START ###############################################
#
#   Base library of common LED Manager functions
#
############################################ INFORMATION SECTION - STOP ################################################

test_ledm_led_config()
{
    fn_name="ledm_lib:test_ledm_led_config"
    log -deb "$fn_name - Turning on WHITE LED"
    led_config_ovsdb on ||
        raise "led_config_ovsdb on" -l "$fn_name" -fc
    check_led_gpio_state on ||
        raise "check_led_gpio_state on" -l "$fn_name" -fc
    sleep 1

    log -deb "$fn_name - Turning LED off"
    led_config_ovsdb off ||
        raise "led_config_ovsdb off" -l "$fn_name" -fc
    check_led_gpio_state off ||
        raise "check_led_gpio_state off" -l "$fn_name" -fc
    sleep 1

    log -deb "$fn_name - LED mode blink"
    led_config_ovsdb blink ||
        raise "led_config_ovsdb blink" -l "$fn_name" -fc
    sleep 5

    log -deb "$fn_name - LED mode breathe"
    led_config_ovsdb breathe ||
        raise "led_config_ovsdb breathe" -l "$fn_name" -fc
    sleep 5

    log -deb "$fn_name - LED mode pattern"
    led_config_ovsdb pattern ||
        raise "led_config_ovsdb pattern" -l "$fn_name" -fc
    sleep 5

    led_config_ovsdb off ||
        raise "led_config_ovsdb off" -l "$fn_name" -fc
    check_led_gpio_state off ||
        raise "check_led_gpio_state off" -l "$fn_name" -fc
}

led_config_ovsdb()
{
    log -deb "This device is not supported! Passing!"
    return 0
}

check_led_gpio_state()
{
    log -deb "This device is not supported! Passing!"
    return 0
}

