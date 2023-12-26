#!/usr/bin/env python3
'''
Module 0-simple_helper_function.py for pagination
'''
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''
    function that returns a tuple of size two containing a start index
    and an end index corresponding to the ranges of indexes to return a list
    for those particular pagination params.
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
