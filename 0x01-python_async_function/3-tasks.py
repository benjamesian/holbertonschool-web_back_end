#!/usr/bin/env python3
"""Basic async function"""
from asyncio import create_task, Task

WAIT_RANDOM = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Create async task"""
    return create_task(WAIT_RANDOM(max_delay))
