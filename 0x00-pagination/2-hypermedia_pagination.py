#!/usr/bin/env python3

"""
module contains these objects:
    1. function `index_range`
    2. class `Server`
"""

import csv
import math
from typing import Dict, List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    takes two integer arguments `page` and `page_size`
    returns a tuple of size two containing a start index and an end index
        corresponding to the range of indexes to return in a list for those
        particular pagination parameters. Page numbers are 1-indexed
    args:   page: int
            page_size: int
    return  index_tuple: Tuple[int, int]
    """
    index_tuple: Tuple[int, int] = (0, 0)
    if ((page < 1) or (page_size < 1)):
        return (index_tuple)
    start: int = ((page - 1) * page_size)
    end: int = (page * page_size)
    index_tuple = (start, end)
    return (index_tuple)


class Server:
    """
    Server class to paginate a database of popular baby names.
    attributes: DATA_FILE
    methods:    __init__
                dataset
                get_page
                get_hyper
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        class constructor
        attributes: self.__dataset
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        args:   page: int
                page_size: int
        return: page_data: List[list]
        """
        page_list: List = []
        try:
            assert isinstance(page, int) and page > 0
            assert isinstance(page_size, int) and page_size > 0
        except AssertionError:
            raise
        page_indexes: Tuple[int, int] = index_range(page, page_size)
        start, end = page_indexes
        page_list = self.dataset()[start:end]
        return (page_list)

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        args:   page: int
                page_size: int
        return: hyper_dict: Dict
        """
        data_size: int = len(self.dataset())
        data: List = self.get_page(page, page_size)
        if ((page * page_size) > data_size):
            next_page = None
        else:
            next_page = (page + 1)
        if (page < 2):
            prev_page = None
        else:
            prev_page = (page - 1)
        total_pages: int = math.ceil((data_size / page_size))
        hyper_dict: Dict = {"page_size": len(data),
                            "page": page,
                            "data": data,
                            "next_page": next_page,
                            "prev_page": prev_page,
                            "total_pages": total_pages,
                            }

        return (hyper_dict)
