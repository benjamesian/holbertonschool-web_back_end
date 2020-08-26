#!/usr/bin/env python3
"""test GithubOrgClient"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """test github client"""

    @parameterized.expand([
        ("google", {"payload": True}),
        ("abc", {"payload": True})
    ])
    @patch("client.get_json")
    def test_org(self, org, payload, mock_get_json):
        """GithubOrgClient.org should return correct value"""
        mock_get_json.return_value = payload
        client = GithubOrgClient(org)
        resp = client.org
        self.assertEqual(payload, resp)
        mock_get_json.assert_called_once()
