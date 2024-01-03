#!/usr/bin/env python3
'''
Module 1-fifo_cache: fifo caching
'''
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    ''' derived class BasicCache inherits from BaseCaching
    and is a caching system, implementing FIFO algo '''

    def __init__(self):
        ''' constructor method '''
        super().__init__()

    def put(self, key, item):
        ''' method to add key, item to cached data '''
        if key is not None or item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS \
                    and key not in self.cache_data.keys():
                first = next(iter(self.cache_data.keys()))
                del self.cache_data[first]
                print(f'DISCARD: {first}')
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        ''' retrieve item linked to key in self.cache_data '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
