#!/usr/bin/env python3
"""Using parameterized library with testing"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Using parameterized library"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, a, b, c):
        """test access_nested_map"""
        self.assertEqual(access_nested_map(a, b), c)
