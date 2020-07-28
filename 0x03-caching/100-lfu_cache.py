#!/usr/bin/python3
"""5. LFU Caching"""
from collections import Counter
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Cache"""

    def __init__(self):
        super().__init__()
        self.keys = set()
        self.counter = Counter()

    def put(self, key, item):
        """Add data to the cache"""
        if key is None or item is None:
            return

        if key in self.counter:
            self.counter[key] = 0
        elif len(self.cache_data) >= self.MAX_ITEMS:
            common = self.counter.most_common()
            i = len(self.counter) - 1
            while i > 0:
                if common[i][1] != common[i - 1][1]:
                    break
                i -= 1
            to_discard = common[i][0]
            print("DISCARD: {}".format(to_discard))
            del self.cache_data[to_discard]
            del self.counter[to_discard]

        self.counter[key] += 1
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve data from the cache"""
        if key is None or key not in self.cache_data:
            return None

        self.counter[key] += 1

        return self.cache_data[key]
