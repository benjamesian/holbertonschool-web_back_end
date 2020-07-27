#!/usr/bin/python3
"""2. LIFO caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFO Cache"""

    def __init__(self):
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add data to the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            to_discard = self.keys.pop()
            print("DISCARD: {}".format(to_discard))
            del self.cache_data[to_discard]

        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
