test_cfg = {
    "um_config": {
        "fw_name": "sc_f5280.scos.oper.gsdf",
    },
    # "um_corrupt_image": [
    #     {
    #         "test_script_timeout": 60,
    #         "fw_path":"/tmp/pfirmware/",
    #     },
    # ],
    "um_corrupt_md5_sum": [
        {
            "test_script_timeout": 120,
        },
    ],
    "um_missing_md5_sum": [
        {
            "test_script_timeout": 120,
            "fw_path":"/tmp/pfirmware/",
        },
    ],    
    "um_download_image_while_downloading": [
        {
            "fw_dl_timer": 30,
            "test_script_timeout": 120,
            "fw_path":"/tmp/pfirmware/",
        },
    ],
    "um_set_correct_firmware_pass": [
        {
            "fw_pass": "correct_fw_pass",
            "fw_url": "url_to_fw_that_require_pass",
        },
    ],
    "um_set_invalid_firmware_pass": [
        {
            "test_script_timeout": 120,
            "fw_pass": "incorrect_fw_pass",
        },
    ],

    "um_set_firmware_url": [
        {
            "test_script_timeout": 120,
            "fw_path":"/tmp/pfirmware/",
            "fw_pass": "incorrect_fw_pass",
        },
    ],

    "um_set_invalid_firmware_url": [
        {
            "test_script_timeout": 120,
        },
    ],
    "um_set_upgrade_dl_timer": [
        {
            "fw_dl_timer": 100,
            "test_script_timeout": 120,
        },
        {
            "fw_dl_timer": 10,
            "test_script_timeout": 20,
        },
    ],
    "um_set_upgrade_timer": [
        {
            "fw_up_timer": 10,
            "test_script_timeout": 120,
        },
    ],
}
