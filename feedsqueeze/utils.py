# -*- coding: utf-8 -*-

"""
feedsqueeze.utils
-----------------

Utility functions for FeedSqueeze.
"""
import os

from jinja2 import Environment, PackageLoader

from . import __title__
from .exceptions import FeedFileDoesNotExist

def get_feed_list_from_file(feed_file):
    """
    Parse given file and return dict.
    """
    if not os.path.exists(feed_file):
        raise FeedFileDoesNotExist

    with open(feed_file) as f:
        list_of_feeds = f.read().splitlines()

    return list_of_feeds


def render_template(filename, context={}, loc=(__title__.lower(), 'templates')):
    env = Environment(loader=PackageLoader(loc[0], loc[1]))
    template = env.get_template(filename)
    return template.render(context)
