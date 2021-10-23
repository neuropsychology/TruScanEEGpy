# -*- coding: utf-8 -*-

"""Submodule."""


def convert_to_tenfive(ch_names=None):
    """Convert channel names to 10-5 system

    This function aims to convert the channel labeling (in number) to the standardized 10-5 electrode labeling.

    Examples
    --------
    >>> import TruScanEEGpy
    >>> import mne
    >>>
    >>> ch = TruScanEEGpy.convert_to_tenfive()
    >>>
    >>> # Compare to other standard montages
    >>> montage = mne.channels.make_standard_montage('standard_1005')
    >>> montage.ch_names
    >>> mne.viz.plot_montage(montage)
    >>>
    >>> montage = mne.channels.make_standard_montage('biosemi128')
    >>> montage.get_positions()
    >>> mne.viz.plot_montage(montage)
    >>>
    >>> montage = mne.channels.make_standard_montage('GSN-HydroCel-128')
    >>> montage.get_positions()
    >>> mne.viz.plot_montage(montage)
    """
    correspondance = {
        # ------------
        "65": "Fpz",
        "1": "Fp1",
        "2": "Fp2",
        # ------------
        "66": "AFp1",
        "67": "AFp2",
        "33": "AF7",
        "34": "AF3",
        "68": "AFz",
        "36": "AF4",
        "38": "AF8",
        # ------------
        "69": "AFF2",
        "70": "AFF1",
        "71": "AFF3",
        "72": "AFF4",
        # ------------
        "3": "F7",
        "41": "F5",
        "4": "F3",
        "43": "F1",
        "5": "Fz",
        "46": "F2",
        "6": "F4",
        "48": "F6",
        "7": "F8",
        # ------------
        "73": "FFT9",
        "74": "FFT7",
        "75": "FFC5",
        "76": "FFC3",
        "77": "FFC1",
        "78": "FFC2",
        "79": "FFC4",
        "80": "FFC6",
        "81": "FFT8",
        "82": "FFT10",
        # ------------
        "50": "FT9",
        "51": "FT7",
        "20": "FC5",
        "35": "FC3",
        "21": "FC1",
        "83": "FCz",
        "22": "FC2",
        "39": "FC4",
        "23": "FC6",
        "40": "FT8",
        "44": "FT10",
        # ------------
        "84": "FTT9",
        "85": "FTT7",
        "86": "FCC5",
        "87": "FCC3",
        "88": "FCC1",
        "89": "FCC2",
        "90": "FCC4",
        "91": "FCC6",
        "92": "FTT8",
        "93": "FTT10",
        # ------------
        "8": "T7",
        "45": "C5",
        "9": "C3",
        "49": "C1",
        "10": "Cz",
        "42": "C2",
        "11": "C4",
        "37": "C6",
        "12": "T8",
        # ------------
        "94": "TTP7",
        "95": "CCP5",
        "96": "CCP3",
        "97": "CCP1",
        "98": "CCP2",
        "99": "CCP4",
        "100": "CCP6",
        "101": "TTP8",
        # ------------
        "47": "TP7",
        "25": "CP5",
        "52": "CP3",
        "26": "CP1",
        "53": "CPz",
        "27": "CP2",
        "54": "CP4",
        "28": "CP6",
        "55": "TP8",
        # ------------
        "102": "TPP9",
        "103": "TPP7",
        "104": "CPP5",
        "105": "CPP3",
        "106": "CPP1",
        "107": "CPP2",
        "108": "CPP4",
        "109": "CPP6",
        "110": "TPP8",
        "111": "TPP10",
        # ------------
        "13": "P7",
        "56": "P5",
        "14": "P3",
        "57": "P1",
        "15": "Pz",
        "58": "P2",
        "16": "P4",
        "59": "P6",
        "17": "P8",
        "112": "P9",
        "119": "P10",
        # ------------
        "24": "TP9",
        "29": "TP10",
        # ------------
        "113": "PPO5",
        "114": "PPO3",
        "115": "PPO1",
        "116": "PPO2",
        "117": "PPO4",
        "118": "PPO6",
        # ------------
        "31": "PO9",
        "60": "PO7",
        "61": "PO3",
        "62": "POz",
        "63": "PO4",
        "64": "PO8",
        "32": "PO10",
        # ------------
        "121": "POO1",
        "122": "POO2",
        "120": "POO3",
        "123": "POO4",
        # ------------
        "18": "O1",
        "30": "Oz",
        "19": "O2",
        # ------------
        "124": "OI1",
        "125": "OI2",
        # ------------
        "126": "I1",
        "127": "Iz",
        "128": "I2",
    }
    if ch_names is None:
        ch_names = list(correspondance.keys())
    ch_names = [correspondance.get(name, name) for name in ch_names]
    return ch_names
