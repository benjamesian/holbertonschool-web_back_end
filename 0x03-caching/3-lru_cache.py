#!/usr/bin/python3
"""3. LRU Caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Cache !!!"""

    def __init__(self):
        """Initialize
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        """Add data to the cache"""
        if key is None or item is None:
            return

        if key in self.keys:
            self.keys.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            to_discard = self.keys.pop(0)
            print("DISCARD: {}".format(to_discard))
            del self.cache_data[to_discard]

        self.keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve data from the cache"""
        if key is None or key not in self.cache_data:
            return None

        self.keys.remove(key)
        self.keys.append(key)

        return self.cache_data[key]
