# -*- coding: utf-8 -*-

"""
lassie.helpers
~~~~~~~~~~~~~~

This module contains the set of helper functions executed by Lassie methods.

"""

import re

CLEANER = re.compile(r'[\r\n\t]')

def clean_text(value):
    return CLEANER.sub('', value)
