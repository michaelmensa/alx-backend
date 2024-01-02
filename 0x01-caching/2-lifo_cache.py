#!/usr/bin/env python3
'''
Module 2-lifo_cache: fifo caching
'''
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    ''' derived class BasicCache inherits from BaseCaching
    implements LIFO algo'''

    def __init__(self):
        ''' constructor method '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' method to add key, item to cached data '''
        if key is not None or Item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                    discard = self.cache_data.popitem(True)
                    print(f'DISCARD: {discard[0]}')
            self.cache_data[key] = item
            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        ''' retrieve item linked to key in self.cache_data '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
