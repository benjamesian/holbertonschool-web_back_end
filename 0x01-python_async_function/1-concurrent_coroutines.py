#!/usr/bin/env python3
"""Basic async function"""
from asyncio import create_task, as_completed
from typing import List

WAIT_RANDOM = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times in parallel"""
    tasks = [create_task(WAIT_RANDOM(max_delay)) for _ in range(n)]
    return [await task for task in as_completed(tasks)]
