"""
Problem ID: 0004
Title: Priority Queue
Difficulty: Easy
Topics: data-structure, heap, agent

Min-priority queue backed by Python's heapq module.
Used as the open-set in A* and Dijkstra.
"""
import heapq
from typing import Any


class PriorityQueue:
    """
    Min-priority queue.

    push(item, priority) — O(log n)
    pop()                — O(log n)  returns item with smallest priority
    peek()               — O(1)
    is_empty()           — O(1)
    """

    def __init__(self) -> None:
        self._heap: list[tuple[float, int, Any]] = []
        self._counter = 0  # tie-breaker so items are never compared

    def push(self, item: Any, priority: float) -> None:
        heapq.heappush(self._heap, (priority, self._counter, item))
        self._counter += 1

    def pop(self) -> Any:
        if self.is_empty():
            raise IndexError("pop from empty PriorityQueue")
        _, _, item = heapq.heappop(self._heap)
        return item

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("peek from empty PriorityQueue")
        return self._heap[0][2]

    def is_empty(self) -> bool:
        return len(self._heap) == 0

    def __len__(self) -> int:
        return len(self._heap)


if __name__ == "__main__":
    pq = PriorityQueue()
    pq.push("node_B", 3)
    pq.push("node_A", 1)
    pq.push("node_C", 2)
    print(pq.pop())  # node_A
    print(pq.pop())  # node_C
    print(pq.pop())  # node_B
    print(pq.is_empty())  # True
