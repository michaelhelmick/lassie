# -*- coding: utf-8 -*-

"""
lassie.api
~~~~~~~~~~

This module contains core Lassie classes and methods.

"""

from bs4 import BeautifulSoup
import requests

from .exceptions import LassieException
from .helpers import strip_tags, clean_text, full_url

import re

OG_META_PATTERN = re.compile(r"^og:(?!image|video)", re.I)
OG_IMAGE_META_PATTERN = re.compile(r"^og:image", re.I)
OG_VIDEO_META_PATTERN = re.compile(r"^og:video", re.I)

TWITTER_META_PATTERN = re.compile(r"^twitter:(?!image)", re.I)
TWITTER_IMAGE_META_PATTERN = re.compile(r"^twitter:image", re.I)

GENERIC_META_PATTERN = re.compile(r"^(description|keywords)", re.I)
APPLE_TOUCH_ICON_PATTERN = re.compile(r"^(apple-touch-icon|apple-touch-icon-precomposed)", re.I)

OG_META_TAGS = {
    'og:url': 'url',
    'og:site_name': 'title',
    'og:description': 'description',
    'og:locale': 'locale',
    'og:image': {
        'og:image': 'src',
        'og:image:width': 'width',
        'og:image:height': 'height',
    },
    'og:video': {
        'og:video': 'src',
        'og:video:width': 'width',
        'og:video:height': 'height',
        'og:video:type': 'type',
    }
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

        soup = BeautifulSoup(html, self.parser)

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
            html = clean_text(response.text)

        return html

    def _get_open_graph_data(self, soup, data):
        open_graph_data = soup.find_all('meta', {'property': OG_META_PATTERN})
        open_graph_image = soup.find_all('meta', {'property': OG_IMAGE_META_PATTERN})
        open_graph_video = soup.find_all('meta', {'property': OG_VIDEO_META_PATTERN})

        for line in open_graph_data:
            key = line.get('property')
            value = line.get('content')

            for prop in OG_META_TAGS:
                if key == prop:
                    data[OG_META_TAGS[prop]] = value

        image = {}
        for line in open_graph_image:
            key = line.get('property')
            value = line.get('content')

            for prop in OG_META_TAGS['og:image']:
                if key == prop:
                    if prop == 'og:image:width' or prop == 'og:image:height':
                        try:
                            value = int(value)
                        except ValueError:
                            value = 0
                    image[OG_META_TAGS['og:image'][prop]] = value

        if image:
            image['type'] = 'og:image'
            data['images'].append(image)

        video = {}
        for line in open_graph_video:
            key = line.get('property')
            value = line.get('content')

            for prop in OG_META_TAGS['og:video']:
                if key == prop:
                    if prop == 'og:video:width' or prop == 'og:video:height':
                        try:
                            value = int(value)
                        except ValueError:
                            value = 0
                    video[OG_META_TAGS['og:video'][prop]] = value

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
                'src': full_url(touch_icon.get('href'), url),
                'type': 'touch_icon'
            })

        return data

    def _get_favicon(self, soup, data, url):
        favicon_data = soup.find_all('link', {'rel': 'icon'})
        for favicon in favicon_data:
            data['images'].append({
                'src': full_url(favicon.get('href'), url),
                'type': 'favicon'
            })

        return data
