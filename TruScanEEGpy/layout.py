# -*- coding: utf-8 -*-

"""Submodule."""
import os
import pandas as pd

from .fix_channels import fix_channels_128
from .convert_channels import tenfive_system_128

def layout_128(names = "index"):
    """Create layout file

    Examples
    --------
    >>> import TruScanEEGpy
    >>>
    >>> layout = TruScanEEGpy.layout_128()
    >>> layout = TruScanEEGpy.layout_128('10-5')
    """
    layout = pd.read_csv(os.path.split(__file__)[0] + '/layouts/deymed_layout_128.txt', sep = '\t')
    layout.columns = layout.columns.str.strip()
    layout["Name"] = fix_channels_128()

    # System
    if names != "index":
        layout["Name"] = tenfive_system_128(layout["Name"])
    return(layout)