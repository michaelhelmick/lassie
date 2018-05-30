# -*- coding: utf-8 -*-

"""
lassie.compat
~~~~~~~~~~~~~

This module contains imports and declarations for seamless Python 2 and
Python 3 compatibility.
"""

import sys

if sys.version_info < (3,):
    from urlparse import urljoin, urlparse
    str = unicode  # noqa: F821
else:
    from urllib.parse import urljoin, urlparse
    str = str


__all__ = [
    'urljoin',
    'urlparse',
    'str'
]
