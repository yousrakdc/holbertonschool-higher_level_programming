#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Class for unittests"""

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)
        self.assertEqual(max_integer([2, 3, -1]), 3)
        self.assertEqual(max_integer([-2, -3, -1]), -1)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([1, 2, 3, -4]), 3)
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)
        self.assertEqual(max_integer([1, 2, 3, 3]), 3)
        self.assertEqual(max_integer([-1]), -1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
