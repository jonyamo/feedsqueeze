# -*- coding: utf-8 -*-

"""
feedsqueeze.main
----------------

Main entry point for FeedSqueeze.
"""
import feedparser
import time

from . import __title__, __version__
from .feed_formats import get_feed_format
from .utils import render_template

def squeeze(list_of_feeds, feed_format=get_feed_format()):
    """
    Feed squeezer.
    """
    squeezed_feed = {
        'title': 'Freshly Squeezed Feed',
        'updated': feed_format.updated(),
        'generator': '{0} {1}'.format(__title__, __version__),
        'entries': []
    }

    for feed_path in list_of_feeds:
        parsed_feed = feedparser.parse(feed_path)
        squeezed_feed['entries'].extend(parsed_feed['entries'])

    squeezed_feed['entries'] = sorted(squeezed_feed['entries'],
                                      key=lambda item: item['published'])

    return render_template(feed_format.template(), {'feed': squeezed_feed})
