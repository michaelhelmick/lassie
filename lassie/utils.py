# -*- coding: utf-8 -*-

"""
lassie.helpers
~~~~~~~~~~~~~~

This module contains the set of helper functions executed by Lassie methods.

"""

import re

CLEANER = re.compile(r'[\r\n\t]')

def clean_text(value):
    """Removes all line breaks, new lines and tabs from the specified content

    :param value: Content to be cleansed
    :type value: string

    """
    return CLEANER.sub('', value)

def convert_to_int(value):
    """Attempts to convert a specified value to an integer

    :param value: Content to be converted into an integer
    :type value: string or int

    """
    try:
        return int(value)
    except TypeError:
        return None
