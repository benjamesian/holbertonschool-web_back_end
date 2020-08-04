#!/usr/bin/env python3
"""0x05. Personal data"""
import bcrypt


def hash_password(pwd: str) -> bytes:
    """Return a hash of a password"""
    return bcrypt.hashpw(bytes(pwd, 'utf-8'), bcrypt.gensalt())


def is_valid(encrypted: bytes, pwd: str) -> bool:
    """Check if a hash matches a password"""
    return bcrypt.checkpw(bytes(pwd, 'utf-8'), encrypted)
