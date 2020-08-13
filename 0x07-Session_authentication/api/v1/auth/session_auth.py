#!/usr/bin/env python3
"""Session Auth
"""
import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Session Authorization
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        if user_id is None or not isinstance(user_id, str):
            return None

        sess_id = str(uuid.uuid4())
        SessionAuth.user_id_by_session_id[sess_id] = user_id
        return sess_id
