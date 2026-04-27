"""
Problem ID : 0003
Title      : Dijkstra's Algorithm
Difficulty : Medium
Topics     : graph, shortest-path, pathfinding
Date       : 2024-01-01
"""

import heapq
from typing import Dict, List, Tuple


def dijkstra(
    graph: Dict[str, List[Tuple[str, float]]],
    source: str,
) -> Dict[str, float]:
    """
    Compute shortest distances from source to all nodes.

    Args:
        graph  : adjacency list {node: [(neighbour, weight), ...]}.
        source : starting node.

    Returns:
        Dict {node: shortest distance from source}.
        Unreachable nodes have distance float("inf").

    Time:  O((V + E) log V)
    Space: O(V)
    """
    dist: Dict[str, float] = {node: float("inf") for node in graph}
    dist[source] = 0.0
    heap: List[Tuple[float, str]] = [(0.0, source)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue  # stale entry
        for v, weight in graph.get(u, []):
            new_dist = dist[u] + weight
            if new_dist < dist.get(v, float("inf")):
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return dist


# ---------------------------------------------------------------------------
# Smoke-test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }
    result = dijkstra(graph, "A")
    print("Distances:", result)
    assert result == {"A": 0, "B": 1, "C": 3, "D": 4}
    print("Smoke-test passed.")
