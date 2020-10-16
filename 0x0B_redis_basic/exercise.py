#!/usr/bin/env python3
"""Redis Caching"""
from typing import Callable, Optional, Union
from uuid import uuid4

from redis.client import Redis


class Cache:

    def __init__(self):
        """Redis cache wrapper"""
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a key, store data at it and return it"""
        key = str(uuid4())
        self._redis.set(key, data)

        return key

    def get(self,
            key: str,
            fn: Optional[Callable]) -> Union[str, bytes, int, float]:
        """Retrieve data stored at a key"""
        value = self._redis.get(key)
        return fn(value) if fn else value

    def get_str(self, key: str) -> str:
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        return self.get(key, int)
