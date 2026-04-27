"""
Problem ID : 0004
Title      : Priority Queue
Difficulty : Easy
Topics     : data-structures, heap
Date       : 2024-01-01
"""

import heapq
from typing import Any, Optional


class MinPriorityQueue:
    """
    Min-priority queue backed by Python's heapq.

    push(item, priority) : O(log n)
    pop()                : O(log n)  — returns item with lowest priority
    peek()               : O(1)      — inspect lowest-priority item
    is_empty()           : O(1)
    """

    def __init__(self) -> None:
        self._heap: list = []
        self._counter: int = 0  # tiebreaker so items are never compared

    def push(self, item: Any, priority: float) -> None:
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("pop from an empty priority queue")
        _, _, item = heapq.heappop(self._heap)
        return item

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("peek at an empty priority queue")
        return self._heap[0][2]

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def __len__(self) -> int:
        return len(self._heap)


# ---------------------------------------------------------------------------
# Smoke-test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    pq = MinPriorityQueue()
    pq.push("explore (2,3)", priority=5)
    pq.push("explore (1,1)", priority=2)
    pq.push("explore (3,4)", priority=8)
    assert pq.peek() == "explore (1,1)"
    assert pq.pop() == "explore (1,1)"
    assert pq.pop() == "explore (2,3)"
    assert pq.pop() == "explore (3,4)"
    assert pq.is_empty()
    print("Smoke-test passed.")
