#!/usr/bin/env python3
"""0x05. Personal data"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Return a hash of a password"""
    return bcrypt.hashpw(bytes(password, 'utf-8'), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if a hash matches a password"""
    return bcrypt.checkpw(bytes(password, 'utf-8'), hashed_password)
