#!/usr/bin/env python3
"""
  concurrent coroutine using tasks
"""

import asyncio
from typing import List

task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        implementation
    """
    result: List[float] = []
    for wait_r_spawn in asyncio.as_completed(
            [task_wait_random(max_delay) for _ in range(n)]):
        result.append(await wait_r_spawn)
    return result
