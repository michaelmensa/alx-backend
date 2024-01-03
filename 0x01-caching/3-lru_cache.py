#!/usr/bin/env python3
'''
Module 3-lru_cache: least recently used caching
'''
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    ''' derived class BasicCache inherits from BaseCaching
    implements LRU algo'''

    def __init__(self):
        ''' constructor method '''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        ''' method to add key, item to cached data '''
        if key is None or item is None:
            pass
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                discard = self.cache_data.popitem(last=False)
                print(f'DISCARD: {discard[0]}')
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        ''' retrieve item linked to key in self.cache_data '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
