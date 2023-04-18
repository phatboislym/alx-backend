#!/usr/bin/env python3
"""
module for class `BasicCache` that inherits from BaseCaching
BasicCache is a caching system without a limit
"""

BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """
    class BasicCache
    methods:    __init__
                put
                get
    """

    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        args:   self
                key: Any
                item: Any
        """
        if (key is None) or (item is None):
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        args:   self
                key: Any
        """
        value = None
        if (key is None) or (key not in self.cache_data):
            return (value)
        value = self.cache_data[key]
        return (value)
