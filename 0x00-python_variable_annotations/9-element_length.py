#!/usr/bin/env python3
"""Annotate a given function"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Given function to annotate"""
    return [(i, len(i)) for i in lst]
