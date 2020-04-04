#!/usr/bin/python3
""" FIFO cache"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Basic LIFO Cache"""

    def __init__(self):
        super().__init__()
        self.lifo_keys = []

    def put(self, key, item):
        """Add an item to the cache"""
        if None in {key, item}:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.lifo_keys.remove(key)
        elif len(self.lifo_keys) >= BaseCaching.MAX_ITEMS:
            remove = self.lifo_keys.pop()
            print("DISCARD: {}".format(remove))
            del self.cache_data[remove]
        self.lifo_keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
