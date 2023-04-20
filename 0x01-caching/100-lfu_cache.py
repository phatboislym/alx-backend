#!/usr/bin/env python3

"""
module for class `LFUCache` that inherits from BaseCaching
`LFUCache` utilizes the Least Frequently Used (LFU) Cache Replacement Policy
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    class LFUCache
    methods:    __init__
                put
                get
    """

    def __init__(self):
        """
        class constructor
        attributes:     self.key_list
                        self.MAX_ITEMS
        """
        super().__init__()
        self.keys = []
        self.hertz = {}

    def put(self, key, item):
        """
        args:   self
                key: Any
                item: Any
        """
        if (key is None) or (item is None):
            return
        elif (key in self.cache_data):
            self.keys.remove(key)
            self.keys.append(key)
            self.cache_data[key] = item
            self.hertz[key] += 1
        elif len(self.cache_data) < self.MAX_ITEMS:
            self.keys.append(key)
            self.cache_data[key] = item
            self.hertz[key] = 1
        else:
            y = min(self.hertz.values())
            for k in list(self.hertz):
                if self.hertz[k] == y:
                    print(f'DISCARD: {k}')
                    del self.cache_data[k]
                    del self.hertz[k]
                    break
            self.cache_data[key] = item
            self.keys.append(key)
            self.hertz[key] = 1

    def get(self, key):
        """
        args:   self
                key: Any
        """
        value = None
        if (key is None) or (key not in self.cache_data):
            return (value)
        if (key in self.keys):
            self.keys.remove(key)
            self.keys.append(key)
            value = self.cache_data[key]
            self.hertz[key] += 1
            return (value)
