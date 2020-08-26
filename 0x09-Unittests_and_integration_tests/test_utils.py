#!/usr/bin/env python3
"""Using parameterized library with testing"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
import utils


class TestAccessNestedMap(unittest.TestCase):
    """Using parameterized library"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, a, b, c):
        """test access_nested_map"""
        self.assertEqual(utils.access_nested_map(a, b), c)

    @parameterized.expand([
        ({}, "a"),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, a, b):
        """parameterized with raised error"""
        with self.assertRaises(KeyError):
            utils.access_nested_map(a, b)


class TestGetJson(unittest.TestCase):
    """parameterized get JSON"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """mock and patch"""

        class MockGet(Mock):
            """mocked requests.get resp"""

            def json(self):
                """resp has json method"""
                return payload

        with patch('utils.requests.get') as mock_get:
            mock_get.return_value = MockGet()
            resp = utils.get_json(url)
            mock_get.assert_called_once_with(url)
            self.assertEqual(resp, payload)


class TestMemoize(unittest.TestCase):
    """mock patch memoize"""

    def test_memoize(self):
        """test memoize util"""

        class TestClass:
            """TestClass for testing purposes only"""

            def a_method(self):
                """test method"""
                return 42

            @utils.memoize
            def a_property(self):
                """only calls test method once"""
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_method:
            obj = TestClass()
            obj.a_property()
            obj.a_property()
            mock_method.assert_called_once()
