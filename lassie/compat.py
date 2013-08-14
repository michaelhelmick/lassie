# -*- coding: utf-8 -*-

"""
lassie.compat
~~~~~~~~~~~~~

This module contains imports and declarations for seamless Python 2 and
Python 3 compatibility.
"""

import sys

_ver = sys.version_info

#: Python 2.x?
is_py2 = (_ver[0] == 2)

#: Python 3.x?
is_py3 = (_ver[0] == 3)

if is_py2:
    from urlparse import urljoin, urlparse

    str = unicode

elif is_py3:
    from urllib.parse import urljoin, urlparse

    str = str
