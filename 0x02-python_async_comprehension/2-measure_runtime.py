#!/usr/bin/env python3
"""
    a coroutine that will execute async_comprehension four times in parallel
    using asyncio.gather, and measure the runtime
"""
from time import perf_counter
import asyncio

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
      implementation
    """
    start: float = perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end: float = perf_counter() - start
    return end
