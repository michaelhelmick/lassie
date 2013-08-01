# -*- coding: utf-8 -*-

"""
lassie.api
~~~~~~~~~~

This module contains core Lassie classes and methods.

"""

from bs4 import BeautifulSoup
import requests

from .compat import urljoin
from .exceptions import LassieException
from .helpers import strip_tags, clean_text

import re

OG_META_PATTERN = re.compile(r"^og:", re.I)
OG_IMAGE_PROPERTY = 'og:image'
OG_VIDEO_PROPERTY = 'og:video'

TWITTER_META_PATTERN = re.compile(r"^twitter:(?!image)", re.I)
TWITTER_IMAGE_META_PATTERN = re.compile(r"^twitter:image", re.I)

GENERIC_META_PATTERN = re.compile(r"^(description|keywords)", re.I)
APPLE_TOUCH_ICON_PATTERN = re.compile(r"^(apple-touch-icon|apple-touch-icon-precomposed)", re.I)

OG_META_TAGS = {
    'og:url': 'url',
    'og:site_name': 'title',
    'og:description': 'description',
    'og:locale': 'locale',

    'og:image': 'src',
    'og:image:width': 'width',
    'og:image:height': 'height',

    'og:video': 'src',
    'og:video:width': 'width',
    'og:video:height': 'height',
    'og:video:type': 'type',
}

TWITTER_META_TAGS = {
    'twitter:url': 'url',
    'twitter:title': 'title',
    'twitter:description': 'description',
    'twitter:locale': 'locale',
    'twitter:image': 'image'
}

GENERIC_META_TAGS = {
    'description': 'description',
    'keywords': 'keywords',
}

class Lassie(object):
    def __init__(self, parser='html5lib'):
        self.parser = parser

    def fetch(self, url, open_graph=True, twitter=True, touch_icon=True, favicon=True, all_images=False):
        """
        {
            'url': 'http://google.com',
            'title': '',
            'description': '',
            'locale': '',
            'images': [{
                'width': 0,
                'height': 0,
                'alt': '',
                'src': '',
                'type': ''
            }],
            'keywords': []
        }
        """

        html = self._retreive_content(url)
        if not html:
            raise LassieException('There was no content to parse.')

        soup = BeautifulSoup(clean_text(html), self.parser)

        data = {
            'images': [],
            'videos': [],
        }

        if open_graph:
            data.update(self._get_open_graph_data(soup, data))

        if twitter:
            data.update(self._get_twitter_data(soup, data))

        data.update(self._get_generic_data(soup, data, url))

        if touch_icon:
            data.update(self._get_touch_icon(soup, data, url))

        if favicon:
            data.update(self._get_favicon(soup, data, url))

        if all_images:
            body_images = soup.findAll('img')
            for image in body_images:
                data['images'].append({
                    'src': image.get('src'),
                    'alt': image.get('alt', ''),
                    'type': 'body_image',
                    'width': int(image.get('width', 0)),
                    'height': int(image.get('height', 0)),
                })

        return data

    def _retreive_content(self, url):
        try:
            response = requests.get(url)
        except requests.exceptions.RequestException as e:
            raise LassieException(e)
        else:
            return response.text

        return ''

    def _get_open_graph_data(self, soup, data):
        open_graph_data = soup.find_all('meta', {'property': OG_META_PATTERN})

        image = {}
        video = {}

        for line in open_graph_data:
            prop = line.get('property')
            value = line.get('content')

            if prop in OG_META_TAGS:
                if prop.startswith((OG_IMAGE_PROPERTY, OG_VIDEO_PROPERTY)) and prop.endswith(('width', 'height')):
                    try:
                        value = int(value)
                    except ValueError:
                        value = 0

                if prop.startswith(OG_IMAGE_PROPERTY):
                    image[OG_META_TAGS[prop]] = value
                elif prop.startswith(OG_VIDEO_PROPERTY):
                    video[OG_META_TAGS[prop]] = value
                elif prop == prop:
                    data[OG_META_TAGS[prop]] = value
        if image:
            image['type'] = OG_IMAGE_PROPERTY
            data['images'].append(image)
        if video:
            data['videos'].append(video)

        return data

    def _get_twitter_data(self, soup, data):
        twitter_data = soup.find_all('meta', {'name': TWITTER_META_PATTERN})
        twitter_image = soup.find_all('meta', {'name': TWITTER_IMAGE_META_PATTERN})

        for line in twitter_data:
            key = line.get('name')
            value = line.get('content')

            for twitter_tag in TWITTER_META_TAGS:
                if key == twitter_tag:
                    data[TWITTER_META_TAGS[twitter_tag]] = value

        for line in twitter_image:
            data['images'].append({
                'src': line.get('content'),
                'type':'twitter:image'
            })

        return data

    def _get_generic_data(self, soup, data, url):
        generic_data = soup.find_all('meta', {'name': GENERIC_META_PATTERN})

        for line in generic_data:
            key = line.get('name', '')
            value = line.get('content')

            for prop in GENERIC_META_TAGS:
                general_key = GENERIC_META_TAGS[prop]
                if key == prop and not general_key in data:
                    if key == 'keywords':
                        value = value.split(',')

                    data[general_key] = value

        if not 'url' in data:
            data['url'] = url

        if not 'title' in data:
            data['title'] = soup.title.string

        return data

    def _get_touch_icon(self, soup, data, url):
        touch_icon_data = soup.find_all('link', {'rel': APPLE_TOUCH_ICON_PATTERN})
        for touch_icon in touch_icon_data:
            data['images'].append({
                'src': urljoin(url, touch_icon.get('href')),
                'type': 'touch_icon'
            })

        return data

    def _get_favicon(self, soup, data, url):
        favicon_data = soup.find_all('link', {'rel': 'icon'})
        for favicon in favicon_data:
            data['images'].append({
                'src': urljoin(url, favicon.get('href')),
                'type': 'favicon'
            })

        return data
