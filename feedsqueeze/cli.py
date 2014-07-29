# -*- coding: utf-8 -*-

"""
FeedSqueeze. Squeeze multiple feeds into one.

Usage: feedsqueeze [--rss | --atom] [-f FILE] [FEED ...]

Specific options:
    --rss        Create new feed using RSS format
    --atom       Create new feed using Atom format (default)
    -f FILE      Path to file containing list of feeds
    FEED ...     List of feeds, separated by spaces

Common options:
    -h --help    Show help
    --version    Show version

"""
import docopt
import os
import sys

from . import __version__
from .main import squeeze
from .feed_formats import get_feed_format
from .utils import get_feed_list_from_file

def main():
    args = docopt.docopt(__doc__, version=__version__)
    feed_format=get_feed_format('rss' if args['--rss'] else 'atom')
    list_of_feeds = []
    if args['-f']:
        list_of_feeds.extend(get_feed_list_from_file(args['-f']))
    if args['FEED']:
        list_of_feeds.extend(args['FEED'])
    print(squeeze(list_of_feeds, feed_format))


if __name__ == '__main__':
    main()

