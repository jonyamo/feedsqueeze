# -*- coding: utf-8 -*-

"""
test_utils
----------

Tests for `feedsqueeze.utils` module.
"""
import sys

if sys.version_info[:2] < (2, 7):
    import unittest2 as unittest
else:
    import unittest

from feedsqueeze import utils
from feedsqueeze.exceptions import FeedFileDoesNotExist

class TestUtils(unittest.TestCase):
    def test_get_feed_list_from_file_missing(self):
        """
        Test that `exceptions.FeedFileDoesNotExist` is thrown when given a file
        that does not exist.
        """
        self.assertRaises(FeedFileDoesNotExist, utils.get_feed_list_from_file,
                          'tests/test-utils/this-does-not-exist.txt')

    def test_get_feed_list_from_file(self):
        """
        Test that given a valid file, a list is returned.
        """
        self.assertEqual(
            utils.get_feed_list_from_file('tests/test-utils/feed_list.txt'),
            ['feed1', 'feed2', 'feed3'])

    def test_render_template(self):
        """
        Test that a properly interpolated string is returned.
        """
        self.assertEqual(
            utils.render_template('template.txt', {'bar':'quux'},
                                  ('tests', 'test-utils')), 'fooquux')


if __name__ == '__main__':
    unittest.main()
