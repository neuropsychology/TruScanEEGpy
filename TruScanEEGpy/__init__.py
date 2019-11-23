# -*- coding: utf-8 -*-

"""Top-level package for TruScanEEGpy."""

# =============================================================================
# Basic
# =============================================================================
import os

__author__ = """TruScanEEGpy developpment team"""
__email__ = 'dom.makowski@gmail.com'
__version__ = '0.0.4'
__modulepath__ = os.path.split(__file__)[0]




# =============================================================================
# Imports
# =============================================================================
from .layouts import *
from .layout import *
from .montage import *
