# -*- coding: utf-8 -*-

"""Submodule."""
import pandas as pd

from .convert_channels import convert_to_tenfive
from .fix_channels import fix_channels_128
from .layouts import Path


def layout_128(names="index"):
    """Create layout file

    Parameters
    ----------
    names : str
        Can be 'index' or '10-5' for the 'mak-128' (an adapated version of 10-5) layout.

    Examples
    --------
    >>> import TruScanEEGpy
    >>>
    >>> layout = TruScanEEGpy.layout_128()
    >>> layout = TruScanEEGpy.layout_128('10-5')
    """
    layout = pd.read_csv(Path.layouts() + "/deymed_layout_128.txt", sep="\t")
    layout.columns = layout.columns.str.strip()
    layout["Name"] = fix_channels_128()

    # System
    if names != "index":
        layout["Name"] = convert_to_tenfive(layout["Name"])
    return layout
