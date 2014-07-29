# -*- coding: utf-8 -*-

"""
feedsqueeze.exceptions
----------------------

All exceptions used in the FeedSqueeze code base.
"""

class FeedSqueezeException(Exception):
    """
    Base exception class. All FeedSqueeze-specific exceptions should
    subclass this class.
    """


class FeedFileDoesNotExist(FeedSqueezeException):
    """
    Raised when given feed_file does not exist.
    """


class InvalidFeedFormat(FeedSqueezeException):
    """
    Raised when given feed format is not valid.
    """
