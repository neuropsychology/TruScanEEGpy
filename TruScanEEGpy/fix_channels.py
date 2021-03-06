# -*- coding: utf-8 -*-

"""Submodule."""

def fix_channels_128(ch_names=None):
    """Returns something something

    Currently, the layout of the channels in the EEG montages found in
    TruScan Acquisition software (v7.8) is mismatched with the layout of the
    channels in the EEG caps. This function attempts to standardize the two
    layouts by re-labelling the channel names in the TruScan Acquisition
    software to the names of the corresponding channels in the cap.
    """
    if ch_names is None:
        ch_names = list(range(1, 128 + 1))
    ch_names = [str(x) for x in ch_names]
    correspondance = {
            "20": "24",
            "21": "29",
            "22": "65",
            "23": "68",
            "24": "83",
            "25": "53",
            "26": "34",
            "27": "36",
            "28": "33",
            "29": "38",
            "31": "60",
            "32": "64",
            "33": "41",
            "34": "43",
            "35": "46",
            "36": "48",
            "37": "51",
            "38": "20",
            "39": "35",
            "40": "21",
            "41": "22",
            "42": "39",
            "43": "23",
            "44": "40",

            "46": "49",
            "47": "42",
            "48": "37",
            "49": "47",
            "50": "25",
            "51": "52",
            "52": "26",
            "53": "27",

            "55": "28",
            "56": "55",
            "57": "56",
            "58": "57",
            "59": "58",
            "60": "59",

            "64": "127",
            "65": "66",
            "66": "67",
            "67": "69",
            "68": "70",
            "69": "71",
            "70": "72",
            "71": "73",
            "72": "74",
            "73": "75",
            "74": "76",
            "75": "77",
            "76": "78",
            "77": "79",
            "78": "80",
            "79": "81",
            "80": "82",
            "81": "50",
            "82": "44",
            "83": "84",
            "84": "85",
            "85": "86",
            "86": "87",
            "87": "88",
            "88": "89",
            "89": "90",
            "90": "91",
            "91": "92",
            "92": "93",
            "93": "94",
            "94": "95",
            "95": "96",
            "96": "97",
            "97": "98",
            "98": "99",
            "99": "100",
            "100": "101",
            "101": "102",
            "102": "103",
            "103": "104",
            "104": "105",
            "105": "106",
            "106": "107",
            "107": "108",
            "108": "109",
            "109": "110",
            "110": "111",
            "111": "112",
            "112": "119",

            "119": "31",
            "120": "32",
            "121": "120",
            "122": "121",
            "123": "122",
            "124": "123",
            "125": "124",
            "126": "125",
            "127": "126"
    }

    ch_names = [correspondance.get(name, name) for name in ch_names]
    return(ch_names)
