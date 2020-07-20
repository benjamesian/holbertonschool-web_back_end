#!/usr/bin/env python3
"""Type annotation practice"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return tuple (k, v^2)"""
    return (k, v**2)
