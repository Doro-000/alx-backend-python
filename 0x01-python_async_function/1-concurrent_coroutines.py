#!/usr/bin/env python3
"""
    an async routine called wait_n that takes in 2 int arguments
    and spawns wait_random with the specified arguments
"""

import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        implementation
    """
    result: List[float] = []
    for wait_r_spawn in asyncio.as_completed(
            [wait_random(max_delay) for _ in range(n)]):
        result.append(await wait_r_spawn)
    return result
