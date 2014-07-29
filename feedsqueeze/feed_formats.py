# -*- coding: utf-8 -*-

"""
feedsqueeze.feed_formats
------------------------

FeedSqueeze feed formats.
"""
import time

from .exceptions import InvalidFeedFormat

def get_feed_format(feed_format='atom'):
    """
    The feed format factory.
    """
    feed_formats = {'atom':AtomFeedFormat,'rss':RssFeedFormat}
    if feed_format in feed_formats:
        return feed_formats[feed_format]()
    else:
        raise InvalidFeedFormat


class FeedFormat():
    def updated(self, time_struct=time.gmtime()):
        return time.strftime(self.DATE_FORMAT, time_struct)

    def template(self):
        return self.TEMPLATE_FILE


class AtomFeedFormat(FeedFormat):
    DATE_FORMAT='%Y-%m-%dT%H:%M:%SZ'
    TEMPLATE_FILE='atom.xml'


class RssFeedFormat(FeedFormat):
    DATE_FORMAT='%a, %d %b %Y %H:%M:%S Z'
    TEMPLATE_FILE='rss.xml'
