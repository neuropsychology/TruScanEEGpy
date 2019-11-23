# -*- coding: utf-8 -*-
"""
layouts submodule.
"""

import inspect

class Path:
    def layouts():
        return(inspect.getfile(Path).split("__init__")[0])