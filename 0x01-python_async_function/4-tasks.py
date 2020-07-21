#!/usr/bin/env python3
"""Basic async function"""
import asyncio
from typing import List

TWR = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times in parallel"""
    return await asyncio.gather(*(TWR(max_delay) for _ in range(n)))
