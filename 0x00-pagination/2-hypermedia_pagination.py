#!/usr/bin/env python3
'''
Module 2-hypermedia_pagination.py: Hypermedia pagination
'''
import csv
import math
from typing import List, Tuple


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        '''
        constructor method
        '''
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        '''
        method that takes tow integer args page and page_size with default
        values 1 and 10 respectively
        '''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # data to paginate
        data = self.dataset()

        # index_range
        idx_range = list(self.index_range(page, page_size))
        return data[idx_range[0]:idx_range[-1]]

    def index_range(self, page: int, page_size: int) -> Tuple:
        '''
        function that returns a tuple of size two containing a start index
        and an end index corresponding to the ranges of indexes to return a
        list
        for those particular pagination params.
        '''
        start_index = (page - 1) * page_size
        end_index = start_index + page_size

        return start_index, end_index

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        ''' method that takes same args and defaults as get_page
        and returns a dict.
        '''
        total_pages = math.ceil(len(self.dataset()) / page_size)
        mini = min(page + 1, total_pages)
        maxi = max(page - 1, 1)
        return {
            'page_size': len(self.get_page(page, page_size)),
            'page': page,
            'data': self.get_page(page, page_size),
            'next_page': mini if page < total_pages else None,
            'prev_page': maxi if page > 1 else None,
            'total_pages': total_pages
        }
