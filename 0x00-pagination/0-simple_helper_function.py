#!/usr/bin/env python3

"""
module for function `index_range`
takes two integer arguments `page` and `page_size`
returns a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters. Page numbers are 1-indexed
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
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
