test_cfg = {
    #####################################
    ## wm2_dfs_cac_aborted
    #####################################
    "wm2_dfs_cac_aborted": [ 
        {
            "channel_A": 56,
            "channel_B": 64,
            "channel_default": 44,
            "ht_mode": "HT20",
            "hw_mode": [
                "11a",
                "11ac",
                "11n",
            ],
        },
    ],
    "wm2_ht_mode_and_channel_iteration": [
        {
            "channels": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
            ],
            "ht_modes": [
                "HT40",
            ],
            "hw_mode": "11n",
        },        
        {
            "channels": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
            ],
            "ht_modes": [
                "HT20",
            ],
            "hw_mode": "11g",
        },
        {
            "channels": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
            ],
            "ht_modes": [
                "HT20",
            ],
            "hw_mode": "11ac",
        },
        {
            "channels": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
            ],
            "ht_modes": [
                "HT20",
            ],
            "hw_mode": "11n",
        },

        # {
        #     "channels": [
        #         36,
        #         40,
        #         44,
        #         48,
        #         52,
        #         56,
        #         60,
        #         64,
        #         100,
        #         104,
        #         108,
        #         112,
        #         116,
        #         120,
        #         124,
        #         128,
        #         132,
        #         136,
        #         140,
        #         149,
        #         153,
        #         157,
        #         161,
        #     ],
        #     "ht_modes": [
        #         "HT40",
        #     ],
        #     "hw_modes": [
        #         "11a",
        #         "11ac",
        #         "11n",
        #     ],
        # },
        # {
        #     "channels": [
        #         36,
        #         40,
        #         44,
        #         48,
        #         52,
        #         56,
        #         60,
        #         64,
        #         100,
        #         104,
        #         108,
        #         112,
        #         116,
        #         120,
        #         124,
        #         128,
        #         132,
        #         136,
        #         140,
        #         149,
        #         153,
        #         157,
        #         161,
        #     ],
        #     "ht_modes": [
        #         "HT80",
        #     ],
        #     "hw_modes": [
        #         "11a",
        #         "11ac",
        #         "11n",
        #     ],
        # },
        # {
        #     "channels": [
        #         36,
        #         40,
        #         44,
        #         48,
        #         52,
        #         56,
        #         60,
        #         64,
        #         100,
        #         104,
        #         108,
        #         112,
        #         116,
        #         120,
        #         124,
        #         128,
        #     ],
        #     "ht_modes": [
        #         "HT160",
        #     ],
        #     "hw_modes": [
        #         "11a",
        #         "11ac",
        #         "11n",
        #     ],
        # },
        {
            "channels": [
                36,
                40,
                44,
                48,
                52,
                56,
                60,
                64,
                100,
                104,
                108,
                112,
                116,
                120,
                124,
                128,
                132,
                136,
                140,
                149,
                153,
                157,
                161,
                165,
            ],
            "ht_modes": [
                "HT20",
            ],
            "hw_mode": "11n",
        },
        {
            "channels": [
                36,
                40,
                44,
                48,
                52,
                56,
                60,
                64,
                100,
                104,
                108,
                112,
                116,
                120,
                124,
                128,
                132,
                136,
                140,
                149,
                153,
                157,
                161,
                165,
            ],
            "ht_modes": [
                "HT20",
            ],
            "hw_mode": "11ac",
        },
        {
            "channels": [
                36,
                40,
                44,
                48,
                52,
                56,
                60,
                64,
                100,
                104,
                108,
                112,
                116,
                120,
                124,
                128,
                132,
                136,
                140,
                149,
                153,
                157,
                161,
                165,
            ],
            "ht_modes": [
                "HT20",
            ],
            "hw_mode": "11a",
        },

    ],
    ################################## MAN CONF 5G Channels ############
    # "wm2_ht_mode_and_channel_iteration_5g_channels": [
    #     {
    #         "channels": [
    #             36,
    #             40,
    #             44,
    #             48,
    #             52,
    #             56,
    #             60,
    #             64,
    #         ],
    #         "ht_modes": [
    #             "HT20",
    #             "HT40",
    #             "HT80",
    #             "HT160",
    #         ],
    #         "hw_mode": "11ax",
    #     },
    #     {
    #         "channels": [
    #             100,
    #             104,
    #             108,
    #             112,
    #             116,
    #             120,120
    #             128,
    #             132,
    #             136,
    #             140,
    #             144,
    #             149,
    #             153,
    #             157,
    #             161,
    #         ],
    #         "ht_modes": [
    #             "HT20",
    #             "HT40",
    #             "HT80",
    #         ],
    #         "hw_mode": "11ax",
    #     },
    # ],
    ###################### END 5G Channels Config #############
    # End Channel Iteration Config
    ##################################
    # Start Radio freq Config
    "wm2_immutable_radio_freq_band": [
        {
            "channel": 157,
            "freq_band": "2.4G",
            "ht_mode": "HT20",
            "hw_mode": "11ac",
        },
        {
            "channel": 1,
            "freq_band": "5G",
            "ht_mode": "HT40",
            "hw_mode": "11n",
        },
    ],
    ##############################################
    #   wm2_immutable_radio_hw_mode
    ##############################################
    "wm2_immutable_radio_hw_mode": [
        {
            "channel": 1,
            "custom_hw_mode": "11b",
            "ht_mode": "HT20",
            "hw_mode": "11n",
        },
        {
            "channel": 36,
            "custom_hw_mode": "11n",
            "ht_mode": "HT40",
            "hw_mode": "11ac",
        },
    ],
    ##############################################
    #   wm2_immutable_radio_hw_type
    ##############################################
    "wm2_immutable_radio_hw_type": [
        {
            "channel": 1,
            "ht_mode": "HT20",
            "hw_mode": "11n",
            "hw_type": "bcm47189",
        },
        {
            "channel": 36,
            "ht_mode": "HT40",
            "hw_mode": "11ac",
            "hw_type": "bcm43684",
        },
    ],
    ##############################################
    #   wm2_set_channel
    ##############################################
    "wm2_set_channel": [
        {
            "channels": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
            ],
            "default_channel": 1,
            "ht_mode": "HT40",
            "hw_mode": "11n",
        },
        {
            "channels": [
                36,
                40,
                44,
                48,
                52,
                56,
                60,
                64,
                100,
                104,
                108,
                112,
                116,
                120,
                124,
                128,
                132,
                136,
                140,
                149,
                153,
                157,
                161,
            ],
            "default_channel": 36,
            "ht_mode": "HT20",
            "hw_mode": "11ac",
        },

    ],
    ##############################################
    #   wm2_set_ht_mode
    ##############################################
    "wm2_set_ht_mode": [
        {
            "channels": [
                2,
                6,
                10,
            ],
            "ht_modes": [
                "HT20",
                "HT40",
            ],
            "hw_mode": "11n",
        },
        {
            "channels": [
                36,
                40,
                44,
                48,
                100,
                104,
                108,
            ],
            "ht_modes": [
                "HT20",
                "HT40",
            ],
            "hw_mode": "11n",
        },
    ],
    ##############################################
    #   wm2_set_radio_country
    ##############################################
    "wm2_set_radio_country": [
        {
            "channel": 1,
            "country": "JP/1",
            "ht_mode": "HT20",
            "hw_mode": "11n",
        },
        # {
        #     "channel": 36,
        #     "country": "JP/0",
        #     "ht_mode": "HT20",
        #     "hw_mode": "11n",
        # },
        # {
        #     "channel": 149,
        #     "country": "JP/0",
        #     "ht_mode": "HT20",
        #     "hw_mode": "11n",
        # },
        # {
        #     "channel": 1,
        #     "country": "EU/1",
        #     "ht_mode": "HT20",
        #     "hw_mode": "11n",
        # },
        # {
        #     "channel": 36,
        #     "country": "EU/0",
        #     "ht_mode": "HT20",
        #     "hw_mode": "11n",
        # },
        # {
        #     "channel": 149,
        #     "country": "EU/0",
        #     "ht_mode": "HT20",
        #     "hw_mode": "11n",
        # },
    ],
    
    ##############################################
    #   wm2_set_radio_enabled
    ##############################################
    "wm2_set_radio_enabled": [
        {
            "channels": [
                1,
                2,
                3,
                4,
                5,
                6,
                7,
                8,
                9,
                10,
                11,
            ],
            "enabled": "false",
            "ht_mode": "HT20",
            "hw_mode": "11n",
        },    
        {
            "channels": [
                36,
                40,
                44,
                48,
                52,
                56,
                60,
                64,
                100,
                104,
                108,
                112,
                116,
                120,
                124,
                128,
                132,
                136,
                140,
                149,
                153,
                157,
                161,
            ],
            "enabled": "false",
            "ht_mode": "HT20",
            "hw_mode": "11n",
        },              
    ],
    ##############################################
    #   wm2_set_radio_tx_power
    ##############################################
    "wm2_set_radio_tx_power": [
        {
            "channel": 1,
            "ht_mode": "HT20",
            "hw_mode": "11n",
            "test_script_timeout": 15,
            "tx_powers": list(range(2, 21)),
        },
        {
            "channel": 36,
            "ht_mode": "HT20",
            "hw_mode": "11a",
            "test_script_timeout": 15,
            "tx_powers": list(range(3, 19)),
        },
    ],
    ##############################################
    #   wm2_set_radio_vif_configs
    ##############################################
    "wm2_set_radio_vif_configs": [
        {
            "channel": 1,
            "custom_channel": 2,
            "ht_mode": "HT20",
            "hw_mode": "11n",
        },
        {
            "channel": 36,
            "custom_channel": 157,
            "ht_mode": "HT20",
            "hw_mode": "11ac",
        },
    ],
    

    ##############################################
    #   wm2_set_bcn_int
    # Test tries to set custom bcn_int (beacon interval)
    #############################################
    "wm2_set_bcn_int": [
        {
            "bcn_int": 200,
            "channel": 2,
            "ht_mode": "HT20",
            "hw_mode": "11n",
        },
        {
            "bcn_int": 400,
            "channel": 36,
            "ht_mode": "HT20",
            "hw_mode": "11ac",
        },
        {
            "bcn_int": 600,
            "channel": 149,
            "ht_mode": "HT20",
            "hw_mode": "11ac",
        },
    ],


    # "wm2_set_radio_thermal_tx_chainmask": [
    #     {
    #         "channel": 2,
    #         "ht_mode": "HT20",
    #         "hw_mode": "11n",
    #         "thermal_tx_chainmask": 2,
    #         "tx_chainmask": 3,
    #     },
    #     {
    #         "channel": 36,
    #         "ht_mode": "HT20",
    #         "hw_mode": "11ac",
    #         "thermal_tx_chainmask": 1,
    #         "tx_chainmask": 3,
    #     },
    #     {
    #         "channel": 149,
    #         "ht_mode": "HT20",
    #         "hw_mode": "11ac",
    #         "thermal_tx_chainmask": 12,
    #         "tx_chainmask": 15,
    #     },
    # ],

    # # Test tries to set tx_chainmask to a custom value. If value is not valid test will fail
    # "wm2_set_radio_tx_chainmask": [
    #     {
    #         "channel": 2,
    #         "ht_mode": "HT20",
    #         "hw_mode": "11n",
    #         "tx_chainmask": 3,
    #     },
    #     {
    #         "channel": 36,
    #         "ht_mode": "HT20",
    #         "hw_mode": "11ac",
    #         "tx_chainmask": 3,
    #     },
    #     {
    #         "channel": 149,
    #         "ht_mode": "HT20",
    #         "hw_mode": "11ac",
    #         "tx_chainmask": 15,
    #     },
    # ],
    ##############################################
    #   wm2_set_ssid
    ##############################################
    "wm2_set_ssid": [
        {
            "channel": 2,
            "ht_mode": "HT20",
            "hw_mode": "11n",
            "ssids": [
                "plus+",
                "minus-",
                "asterisk*",
                "hash#",
                "question_mark?",
                "backslash\\",
                "emoji👍",
                "cyrilicГДИѲЛ",
                "arabic٤ټٽ",
                "hebrewאב",
                "japanese飾り羽",
                "special[\\T/]",
            ],
        },
        {
            "channel": 36,
            "ht_mode": "HT20",
            "hw_mode": "11ac",
            "ssids": [
                "plus+",
                "minus-",
                "asterisk*",
                "hash#",
                "question_mark?",
                "backslash\\",
                "emoji👍",
                "cyrilicГДИѲЛ",
                "arabic٤ټٽ",
                "hebrewאב",
                "japanese飾り羽",
                "special[\\T/]",
            ],
        },
    ],
}

