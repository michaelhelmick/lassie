# -*- coding: utf-8 -*-

"""
lassie.filters
~~~~~~~~~~~~~~

This package contains various filters for parsing content.

"""

from .apple import APPLE_MAPS
from .generic import GENERIC_MAPS
from .social import SOCIAL_MAPS

META_MAPS = dict(list(GENERIC_MAPS['meta'].items()) + list(SOCIAL_MAPS['meta'].items()))
LINK_MAPS = dict(list(APPLE_MAPS['link'].items()) + list(GENERIC_MAPS['link'].items()))

FILTER_MAPS = {
    'meta': META_MAPS,
    'link': LINK_MAPS,
}
