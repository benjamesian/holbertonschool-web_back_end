#!/usr/bin/python3
""" MRU cache"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Basic MRU Cache"""

    def __init__(self):
        super().__init__()
        self.mru_keys = []

    def put(self, key, item):
        """Add an item to the cache"""
        if None in {key, item}:
            return

        if key in self.cache_data:
            self.mru_keys.remove(key)
        elif len(self.mru_keys) >= BaseCaching.MAX_ITEMS:
            remove = self.mru_keys.pop()
            print("DISCARD: {}".format(remove))
            del self.cache_data[remove]

        self.cache_data[key] = item
        self.mru_keys.append(key)

    def get(self, key):
        """Gen an item from the cache"""
        if key in self.cache_data:
            self.mru_keys.remove(key)
            self.mru_keys.append(key)
            return self.cache_data[key]
