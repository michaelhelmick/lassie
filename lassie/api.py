# -*- coding: utf-8 -*-

"""
lassie.api
~~~~~~~~~~

This module implements the Lassie API.

"""

from .core import Lassie

def fetch(url, **kwargs):
    """Constructs and sends a :class:`Lassie <Lassie>`
    Retrieves content from the specified url, parses it, and returns
    a beautifully crafted dictionary of important information about that
    web page.

    Priority tree is as follows:
        1. Open Graph
        2. Twitter Card
        3. Other meta content (i.e. description, keywords)

    :param url: URL to send a GET request to
    :param open_graph: (optional) If ``True``, filters web page content for Open Graph meta tags. The content of these properties have top priority on return values.
    :type open_graph: bool
    :param twitter_card: (optional) If ``True``, filters web page content for Twitter Card meta tags
    :type twitter_card: bool
    :param touch_icon: (optional) If ``True``, retrieves Apple touch icons and includes them in the response ``images`` array
    :type touch_icon: bool
    :param favicon: (optional) If ``True``, retrieves any favicon images and includes them in the response ``images`` array
    :type favicon: bool
    :param all_images: (optional) If ``True``, retrieves images inside web pages body and includes them in the response ``images`` array. Default: False
    :type all_images: bool
    :param parser: (optional) String reference for the parser that BeautifulSoup will use
    :type parser: string
    :param handle_file_content: (optional) If ``True``, lassie will return a generic response when a file is fetched. Default: False
    :type handle_file_content: bool

    """
    l = Lassie()
    return l.fetch(url, **kwargs)
