#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""
import asyncio
from time import perf_counter

ASYNC_COMPREHENSION = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Return time taken to multiple approx 10s async functions in parallel"""
    start = perf_counter()
    await asyncio.gather(*(ASYNC_COMPREHENSION() for _ in range(4)))
    return perf_counter() - start
