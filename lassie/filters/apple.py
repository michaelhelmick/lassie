# -*- coding: utf-8 -*-

"""
lassie.filters.apple
~~~~~~~~~~~~~~~~~~~~

This module contains Apple related content to help Lassie filter for content.

"""

from ..compat import str

import re

APPLE_MAPS = {  # http://i.imgur.com/cla85xT.jpg
    'link': {
        'touch_icon': {
            'pattern': re.compile(r"^(apple-touch-icon|apple-touch-icon-precomposed)", re.I),
            'key': 'icon',
            'type': str('touch_icon'),
        },
    }
}
