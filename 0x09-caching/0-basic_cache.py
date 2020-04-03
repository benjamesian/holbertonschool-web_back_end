#!/usr/bin/python3
""" Basic dictionary """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Basic Cache"""

    def put(self, key, item):
        """Add an item to the cache"""
        if None not in {key, item}:
            self.cache_data[key] = item

    def get(self, key):
        """Get value associated with `key` in the cache"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
