#!/usr/bin/python3
""" FIFO cache"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Basic FIFO Cache"""

    def __init__(self):
        super().__init__()
        self.fifo_keys = []

    def put(self, key, item):
        """Add an item to the cache"""
        if None in {key, item}:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.fifo_keys.remove(key)
        elif len(self.fifo_keys) > BaseCaching.MAX_ITEMS:
            remove = self.fifo_keys.pop(0)
            print("DISCARD: {}".format(remove))
            del self.cache_data[remove]
        self.fifo_keys.append(key)
        self.cache_data[key] = item

    def get(self, key):
        """Get an item from the cache"""
        if key in self.cache_data:
            return self.cache_data[key]
        return None
