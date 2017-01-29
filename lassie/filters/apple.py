# -*- coding: utf-8 -*-

"""
lassie.filters.apple
~~~~~~~~~~~~~~~~~~~~

This module contains Apple related content to help Lassie filter for content.

"""

import re

from ..compat import str

APPLE_MAPS = {  # http://i.imgur.com/cla85xT.jpg
    'link': {
        'touch_icon': {
            'pattern': re.compile(r"^(apple-touch-icon|apple-touch-icon-precomposed)", re.I),
            'key': 'icon',
            'type': str('touch_icon'),
        },
    }
}
