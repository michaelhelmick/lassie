# -*- coding: utf-8 -*-

"""
lassie.helpers
~~~~~~~~~~~~~~

This module contains the set of helper functions executed by Lassie methods.

"""

import re
from urlparse import urljoin

CLEANER = re.compile(r'[\r\n\t]')

def strip_tags(value):
    return re.sub(r'<[^>]*?>', '', value.encode('utf-8'))

def clean_text(value):
    return CLEANER.sub('', value)
