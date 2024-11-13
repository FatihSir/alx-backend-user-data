#!/usr/bin/python3
"""Auth Module"""


from flask import request
from typing import List, TypeVar


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ A method checks if authentication is required"""
        return False

    def authorization_header(self, request=None) -> str:
        """A method for authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """A method for current user"""
        return None
