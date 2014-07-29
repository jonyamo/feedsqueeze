FeedSqueeze
===========

Squeeze multiple feeds into one.

Introduction
------------

FeedSqueeze takes a list of XML feeds and compresses them into one single feed.
The list of feeds can either be passed via the command line or from a config
file. The resulting squeezed feed will simply be written to STDOUT.

Installation
------------

.. code-block:: bash

    $ git clone https://github.com/jonyamo/feedsqueeze.git
    $ cd feedsqueeze
    $ python setup.py install

Usage
-----

Command line:

.. code-block:: bash

    Usage: feedsqueeze [--rss | --atom] [-f FILE] [FEED ...]

    Specific options:
        --rss        Create new feed using RSS format
        --atom       Create new feed using Atom format (default)
        -f FILE      Path to file containing list of feeds
        FEED ...     List of feeds, separated by spaces

As a module:

.. code-block:: python

    from feedsqueeze.main import squeeze

    >>> squeeze(list_of_feeds)
