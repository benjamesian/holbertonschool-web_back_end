#!/usr/bin/python3
""" LRU cache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Basic LRU Cache"""

    def __init__(self):
        super().__init__()
        self.lru_keys = []

    def put(self, key, item):
        """Add an item to the cache"""
        if None in {key, item}:
            return

        if key in self.cache_data:
            self.lru_keys.remove(key)
        elif len(self.lru_keys) >= BaseCaching.MAX_ITEMS:
            remove = self.lru_keys.pop(0)
            del self.cache_data[remove]

        self.cache_data[key] = item
        self.lru_keys.append(key)

    def get(self, key):
        """Gen an item from the cache"""
        if key in self.cache_data:
            return self.cache_data[key]
