"""
0004 – Priority Queue
=====================
Problem: Implement a min-priority queue backed by Python's heapq.
Source:  custom
Difficulty: Easy
Topics: data-structures, heap, priority-queue

Time  complexity: O(log n) push / pop, O(1) peek
Space complexity: O(n)
"""

from __future__ import annotations

import heapq
from typing import Any, Generic, Iterator, List, Tuple, TypeVar

T = TypeVar("T")


class PriorityQueue(Generic[T]):
    """Min-priority queue: smallest priority value is popped first.

    Ties in priority are broken by insertion order (FIFO).

    Examples:
        >>> pq = PriorityQueue()
        >>> pq.push("B", 5)
        >>> pq.push("A", 1)
        >>> pq.push("C", 3)
        >>> pq.pop()
        'A'
        >>> pq.pop()
        'C'
    """

    def __init__(self) -> None:
        self._heap: List[Tuple[Any, int, T]] = []
        self._counter = 0  # tie-breaker

    def push(self, item: T, priority: Any) -> None:
        """Insert *item* with *priority*."""
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1

    def pop(self) -> T:
        """Remove and return the item with the lowest priority.

        Raises IndexError if the queue is empty.
        """
        if not self._heap:
            raise IndexError("pop from an empty priority queue")
        _, _, item = heapq.heappop(self._heap)
        return item

    def peek(self) -> T:
        """Return the item with the lowest priority without removing it.

        Raises IndexError if the queue is empty.
        """
        if not self._heap:
            raise IndexError("peek at an empty priority queue")
        _, _, item = self._heap[0]
        return item

    def __len__(self) -> int:
        return len(self._heap)

    def __bool__(self) -> bool:
        return bool(self._heap)

    def __iter__(self) -> Iterator[T]:
        """Iterate items in priority order (destructive)."""
        while self._heap:
            yield self.pop()


# ---------------------------------------------------------------------------
# Quick self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    pq: PriorityQueue[str] = PriorityQueue()
    pq.push("B", 5)
    pq.push("A", 1)
    pq.push("C", 3)
    print("peek:", pq.peek())  # A
    print("pop:", pq.pop())    # A
    print("pop:", pq.pop())    # C
    print("pop:", pq.pop())    # B
    print("empty:", len(pq) == 0)  # True
