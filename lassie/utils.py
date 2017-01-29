# -*- coding: utf-8 -*-

"""
lassie.helpers
~~~~~~~~~~~~~~

This module contains the set of helper functions executed by Lassie methods.

"""

import locale
import re

from requests.utils import default_user_agent

from .compat import str, urljoin

CLEANER = re.compile(r'[\r\n\t]')
RE_INT = re.compile(r'\d+')
FAKE_USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/603.1.20 (KHTML, like Gecko) Version/10.1 Safari/603.1.20'

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
    if isinstance(value, str):
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

def normalize_image_data(data, url):
    # Create image list then remove duplicate images?
    img = {
        'src': urljoin(url, data.get('src')),
        'alt': data.get('alt', ''),
        'type': u'body_image',
    }

    # Only include width and height if included as an attribute of the element
    width = convert_to_int(data.get('width'))
    if width:
        img['width'] = width

    height = convert_to_int(data.get('height'))
    if height:
        img['height'] = height

    return img

def determine_user_agent(user_agent):
    if not user_agent or  user_agent == default_user_agent():
        return FAKE_USER_AGENT

    return user_agent
