#!/usr/bin/env python3
"""Authorization Class"""
from typing import List, TypeVar
from flask import request


class Auth:
    """Authorization Methods"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Require authentication
        """
        if path is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path += '/'
        return path not in excluded_paths

    def authorization_header(self, request=None) -> str:
        """ Get value of auth header
        """
        if request is None:
            return None
        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """ Get the current user
        """
        return None
