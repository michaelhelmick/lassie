# -*- coding: utf-8 -*-

#     __         ______     ______     ______     __     ______
#    /\ \       /\  __ \   /\  ___\   /\  ___\   /\ \   /\  ___\
#    \ \ \____  \ \  __ \  \ \___  \  \ \___  \  \ \ \  \ \  __\
#     \ \_____\  \ \_\ \_\  \/\_____\  \/\_____\  \ \_\  \ \_____\
#      \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_/   \/_____/

"""
Lassie
------

Lassie is a Python library for retrieving basic content from websites.

"""

__version__ = '0.8.3'

from .api import fetch
from .core import Lassie
from .exceptions import LassieError
