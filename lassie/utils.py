# -*- coding: utf-8 -*-

"""
lassie.helpers
~~~~~~~~~~~~~~

This module contains the set of helper functions executed by Lassie methods.

"""

from .compat import str

import locale
import re

CLEANER = re.compile(r'[\r\n\t]')
RE_INT = re.compile(r'\d+')

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
    if not value:
        return None

    # Apart from numbers also accept values that end with px
    value = value.strip(' px')
    try:
        return int(value)
    except (TypeError, ValueError):
        return None

def normalize_locale(value):
    value = value.replace('-', '_')
    the_locale = locale.normalize(value)

    if the_locale != value:
        # Should we return the actual locale, returned from the locale lib instead of splitting?
        try:
            return str(the_locale.split('.')[0])
        except IndexError:  # pragma: no cover
            pass
    return None

