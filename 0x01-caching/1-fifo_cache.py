#!/usr/bin/env python3
"""
module for class `FIFOCache` that inherits from `BaseCaching`
`FIFOCache` is a caching system with a FIFO Cache Replacement Policy
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCache
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

    def put(self, key, item):
        """
        args:   self
                key: Any
                item: Any
        """
        if (key is None) or (item is None):
            return
        elif (key in self.cache_data):
            self.cache_data[key] = item
        elif len(self.cache_data) < self.MAX_ITEMS:
            self.keys.append(key)
            self.cache_data[key] = item
        else:
            x = self.keys.pop(0)
            del self.cache_data[x]
            print(f'DISCARD: {x}')
            self.cache_data[key] = item
            self.keys.append(key)

    def get(self, key):
        """
        args:   self
                key: Any
        """
        value = None
        if (key is None) or (key not in self.cache_data):
            return (value)
        if (key in self.keys):
            value = self.cache_data[key]
            return (value)
