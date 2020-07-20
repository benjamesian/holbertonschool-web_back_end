#!/usr/bin/env python3
"""Type annotated list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """Return the sum of a list of numbers"""
    return sum(mxd_lst)
