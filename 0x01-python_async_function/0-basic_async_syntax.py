#!/usr/bin/env python3
"""Basic async function"""
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait between 0 and max_delay seconds and return the amount of time waited
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
