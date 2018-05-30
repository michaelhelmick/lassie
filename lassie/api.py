# -*- coding: utf-8 -*-

"""
lassie.api
~~~~~~~~~~

This module implements the Lassie API.

"""

from lassie.core import Lassie


lassie = Lassie()


def fetch(url, **kwargs):
    return lassie.fetch(url, **kwargs)


fetch.__doc__ = 'Fetches from a default :class:`Lassie` instance.\n\n' + \
                Lassie.fetch.__doc__


__all__ = [fetch.__name__]
