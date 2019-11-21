# -*- coding: utf-8 -*-

"""Submodule."""
import mne
import pandas as pd
import numpy as np

from .fix_channels import fix_channels_128
from .convert_channels import tenfive_system_128

def montage_mne_128(layout):
    """Create MNE montage

    Examples
    --------
    >>> import TruScanEEGpy
    >>> import mne
    >>>
    >>> layout = TruScanEEGpy.layout_128()
    >>> montage = TruScanEEGpy.montage_mne_128(layout)
    >>> mne.viz.plot_montage(montage)
    >>> mne.viz.plot_montage(montage, kind = "3d")
    """
    layout["ID"] = layout["Name"]
    layout = layout.set_index('Name')
    layout = layout.to_dict(orient = "index")
    for channel in layout.keys():
        yxz = np.array([layout[channel]["Y"], -1*layout[channel]["X"], layout[channel]["Z"]])
        layout[channel] = yxz
    montage = mne.channels.make_dig_montage(layout, coord_frame='head')
    return(montage)
