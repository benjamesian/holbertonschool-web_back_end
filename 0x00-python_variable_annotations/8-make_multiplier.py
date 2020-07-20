#!/usr/bin/env python3
"""Type annotation practice"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Make a multiplier"""
    return lambda mul: mul * multiplier
