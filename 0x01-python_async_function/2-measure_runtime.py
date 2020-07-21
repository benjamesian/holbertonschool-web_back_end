#!/usr/bin/env python3
"""Basic async function"""
import asyncio
import time

WAIT_N = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Contrived async example"""
    start = time.perf_counter()
    asyncio.run(WAIT_N(n, max_delay))
    return (time.perf_counter() - start) / n
