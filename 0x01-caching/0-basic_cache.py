#!/usr/bin/env python3
'''
Module 0-basic_cache: basic dictionary
'''
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    ''' derived class BasicCache inherits from BaseCaching
    and is a caching system '''

    def put(self, key, item):
        ''' method to add key, item to cached data '''
        if key is not None or item is not None:
            self.cache_data[key] = item

    def get(self, key):
        ''' retrieve item linked to key in self.cache_data '''
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
