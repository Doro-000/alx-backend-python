#!/usr/bin/env python3
"""
    a coroutine that will loop 10 times, each time asynchronously
    waits 1 second, and then yields a random number between 0 and 10
"""
from typing import Generator
import random
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """
      implementation
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
