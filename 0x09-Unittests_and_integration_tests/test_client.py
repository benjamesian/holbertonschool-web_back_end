#!/usr/bin/env python3
"""test GithubOrgClient"""
import unittest
from unittest.mock import patch, PropertyMock
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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)])
    def test_has_license(self, repo, lisc_key, out):
        """test_has_liscence"""
        client = GithubOrgClient("google")
        res = client.has_license(repo, lisc_key)
        self.assertEqual(res, out)
