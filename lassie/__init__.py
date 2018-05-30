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

__version__ = '0.11.6'

from lassie.api import fetch
from lassie.core import Lassie
from lassie.exceptions import LassieError

__all__ = [
    fetch.__name__,
    Lassie.__name__,
    LassieError.__name__,
]
