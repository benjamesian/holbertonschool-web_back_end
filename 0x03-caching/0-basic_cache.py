#!/usr/bin/python3
"""0. Basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Standard dictionary"""

    def put(self, key, item):
        """Put item in the dictionary"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve item from the dictionary"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
