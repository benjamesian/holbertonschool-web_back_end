#!/usr/bin/env python3
"""Redis Caching"""
from functools import wraps
from typing import Callable, Optional, Union
from uuid import uuid4

from redis.client import Redis


def replay(method: Callable):
    """Replay decorated method history"""
    method_name = method.__qualname__
    i = method_name + ":inputs"
    o = method_name + ":outputs"
    inst = method.__self__
    count = inst.get(method_name)
    print(f"{method_name} was called {count.decode('utf-8')} times:")

    inputs = inst._redis.lrange(i, 0, -1)
    outputs = inst._redis.lrange(o, 0, -1)
    for k, v, in zip(inputs, outputs):
        print(f"{method_name}(*{k.decode('utf-8')}) -> {v.decode('utf-8')}")


def count_calls(method: Callable) -> Callable:
    """Count calls of Cache methods"""

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Store Cache method inputs and outputs"""
    method_name = method.__qualname__
    i = method_name + ":inputs"
    o = method_name + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function"""
        self._redis.rpush(i, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(o, str(result))
        return result

    return wrapper


class Cache:

    def __init__(self):
        """Redis cache wrapper"""
        self._redis = Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generate a key, store data at it and return it"""
        key = str(uuid4())
        self._redis.set(key, data)

        return key

    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """Retrieve data stored at a key"""
        value = self._redis.get(key)
        return fn(value) if fn else value

    def get_str(self, key: str) -> str:
        """get a string"""
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """get an int"""
        return self.get(key, int)
