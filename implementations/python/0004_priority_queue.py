"""
Problem: Priority Queue
ID: 0004
Difficulty: Easy
Topics: data-structures, heap

A stable min-priority queue backed by heapq.  Equal-priority items are
returned in FIFO (insertion) order.

Class:
    PriorityQueue
"""

import heapq
from typing import Any, Optional


class PriorityQueue:
    """
    Stable min-priority queue.

    Uses a monotonically-increasing counter as a tie-breaker so that items
    with equal priority are dequeued in insertion order (FIFO).

    Operations:
        push(item, priority) — O(log n)
        pop()                — O(log n)
        peek()               — O(1)
        __len__()            — O(1)
        __bool__()           — O(1)
    """

    def __init__(self) -> None:
        self._heap: list = []
        self._counter: int = 0

    def push(self, item: Any, priority: float = 0) -> None:
        """Add item with given priority (lower value = higher priority)."""
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1

    def pop(self) -> Any:
        """Remove and return the lowest-priority item."""
        if not self._heap:
            raise IndexError("pop from empty PriorityQueue")
        _, _, item = heapq.heappop(self._heap)
        return item

    def peek(self) -> Any:
        """Return the lowest-priority item without removing it."""
        if not self._heap:
            raise IndexError("peek at empty PriorityQueue")
        return self._heap[0][2]

    def __len__(self) -> int:
        return len(self._heap)

    def __bool__(self) -> bool:
        return bool(self._heap)
