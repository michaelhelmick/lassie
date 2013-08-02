# -*- coding: utf-8 -*-

#     __         ______     ______     ______     __     ______
#    /\ \       /\  __ \   /\  ___\   /\  ___\   /\ \   /\  ___\
#    \ \ \____  \ \  __ \  \ \___  \  \ \___  \  \ \ \  \ \  __\
#     \ \_____\  \ \_\ \_\  \/\_____\  \/\_____\  \ \_\  \ \_____\
#      \/_____/   \/_/\/_/   \/_____/   \/_____/   \/_/   \/_____/

"""
lassie.filters
~~~~~~~~~~~~~~

This package contains various filters for parsing content.

"""

import re

from .generic import GENERIC_MAPS
from .social import SOCIAL_MAPS

APPLE_TOUCH_ICON_PATTERN = re.compile(r"^(apple-touch-icon|apple-touch-icon-precomposed)", re.I)
FILTER_MAPS = dict(GENERIC_MAPS.items() + SOCIAL_MAPS.items())
