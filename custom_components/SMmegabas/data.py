FULL_NAME="Building Automation"
LINK="https://sequentmicrosystems.com/products/building-automation-8-layer-stackable-hat-v4-for-raspberry-pi"

import megabas
API = megabas
DOMAIN = "SMmegabas"
NAME_PREFIX = "smmb"
SM_MAP = {
    #"button": {
    #    "contact_cnt_rst": {
    #        "chan_no": 4,
    #        "com": {
    #            "set": "rstContactCounter",
    #        },
    #    }
    #},
    "binary_sensor": {
        "contact": {
            "chan_no": 4,
            "uom": "",
            "com": {
                "get": "getContactCh",
            },
        },
    },
    "sensor":  {
        "u_in": {
                "chan_no": 8,
                "uom": "V",
                "com": {
                    "get": "getUIn",
                },
        },
        "r1k": {
                "chan_no": 8,
                "uom": "kOwm",
                "com": {
                    "get": "getRIn1K",
                },
        },
        "r10k": {
                "chan_no": 8,
                "uom": "kOwm",
                "com": {
                    "get": "getRIn10K",
                },
        },
        "contact_cnt": {
                "chan_no": 4,
                "uom": "",
                "com": {
                    "get": "getContactCounter",
                },
        },
        "card_volt": {
                "chan_no": 1,
                "uom": "V",
                "com": {
                    "get": "getInVolt",
                },
        },
        "rasp_volt": {
                "chan_no": 1,
                "uom": "V",
                "com": {
                    "get": "getRaspVolt",
                },
        },
        "cpu_temp": {
                "chan_no": 1,
                "uom": "°C",
                "com": {
                    "get": "getCpuTemp",
                },
        }
    },
    "switch": {
        "triac": {
                "chan_no": 4,
                "com": {
                    "get": "getTriac",
                    "set": "setTriac",
                },
        }
    },
    "number": {
        "u_out": {
                "chan_no": 4,
                "uom": "V",
                "min_value": 0.0,
                "max_value": 10.0,
                "step": 0.01,
                "com": {
                    "get": "getUOut",
                    "set": "setUOut",
                },
        },
        "4_20_i_out": {
                "chan_no": 4,
                "uom": "mA",
                "min_value": 4.0,
                "max_value": 20.0,
                "step": 0.01,
                "com": {
                    "get": "get4_20Out",
                    "set": "set4_20Out",
                },
        },
        "od": {
                "chan_no": 4,
                "uom": "%",
                "min_value": 0.0,
                "max_value": 100.0,
                "step": 0.01,
                "com": {
                    "get": "getOdPWM",
                    "set": "setOdPWM"
                },
                "icon": {
                    "on": "mdi:percent",
                    "off": "mdi:percent"
                }
        },
    },
}
