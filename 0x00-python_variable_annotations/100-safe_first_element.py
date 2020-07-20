#!/usr/bin/env python3
"""Add duck typed annotations"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Annotated function"""
    if lst:
        return lst[0]
    else:
        return None
