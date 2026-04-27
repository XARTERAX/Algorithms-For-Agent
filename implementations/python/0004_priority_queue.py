"""
0004 – Min-Priority Queue
===========================
Topic      : data structures / heap
Difficulty : Easy

Problem
-------
Implement a min-priority queue backed by Python's heapq.  Supports:
  push(item, priority)  – O(log n)
  pop()                 – O(log n)
  peek()                – O(1)
  is_empty()            – O(1)

Examples
--------
>>> pq = MinPriorityQueue()
>>> pq.push("A", 3); pq.push("B", 1); pq.push("C", 2)
>>> pq.pop()
'B'
>>> pq.peek()
'C'

Complexity
----------
Time : O(log n) push / pop;  O(1) peek
Space: O(n)
"""

import heapq
from typing import Any, List, Tuple


class MinPriorityQueue:
    """Min-priority queue using a binary heap.

    Items with the same priority are returned in insertion order (FIFO).
    """

    def __init__(self) -> None:
        self._heap: List[Tuple[float, int, Any]] = []
        self._counter: int = 0  # tie-breaker for equal priorities

    def push(self, item: Any, priority: float) -> None:
        """Insert *item* with *priority*."""
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1

    def pop(self) -> Any:
        """Remove and return the item with the lowest priority.

        Raises
        ------
        IndexError
            If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("pop from an empty priority queue")
        _, _, item = heapq.heappop(self._heap)
        return item

    def peek(self) -> Any:
        """Return (without removing) the item with the lowest priority.

        Raises
        ------
        IndexError
            If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("peek at an empty priority queue")
        return self._heap[0][2]

    def is_empty(self) -> bool:
        """Return True if the queue contains no items."""
        return len(self._heap) == 0

    def __len__(self) -> int:
        return len(self._heap)


# ---------------------------------------------------------------------------
# Quick smoke test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    pq = MinPriorityQueue()
    pq.push("A", 3)
    pq.push("B", 1)
    pq.push("C", 2)
    print("pop:", pq.pop())   # B
    print("peek:", pq.peek())  # C
    print("pop:", pq.pop())   # C
    print("pop:", pq.pop())   # A
    print("empty:", pq.is_empty())
