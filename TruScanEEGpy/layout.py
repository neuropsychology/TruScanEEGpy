# -*- coding: utf-8 -*-

"""Submodule."""
import os
import pandas as pd

from .fix_channel_names import fix_channel_names_128


def layout_128():
    layout = pd.read_csv(os.path.split(__file__)[0] + '/layouts/deymed_layout_128.txt', sep = '\t')
    layout.columns = layout.columns.str.strip()
    layout["Name"] = fix_channel_names_128()
    return(layout)