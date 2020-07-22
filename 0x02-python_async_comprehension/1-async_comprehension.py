#!/usr/bin/env python3
"""1. Async Comprehensions"""
from typing import List

ASYNC_GENERATOR = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Use async list comprehension and generate a list of random numbers"""
    return [rand async for rand in ASYNC_GENERATOR()]
