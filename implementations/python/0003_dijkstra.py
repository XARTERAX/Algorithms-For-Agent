"""
0003 – Dijkstra Shortest Path
==============================
Problem: Single-source shortest paths on a weighted directed graph
         with non-negative edge weights.
Source:  custom
Difficulty: Medium
Topics: graph, shortest-path, priority-queue

Time  complexity: O((V + E) log V)
Space complexity: O(V + E)
"""

from __future__ import annotations

import heapq
from typing import Dict, List, Tuple

Graph = Dict[int, List[Tuple[int, float]]]  # node -> [(neighbour, weight)]


def dijkstra(graph: Graph, source: int) -> Dict[int, float]:
    """Return shortest distances from *source* to all reachable nodes.

    Unreachable nodes are not included in the result dict.

    Args:
        graph: adjacency list {node: [(neighbour, weight), ...]}.
               All weights must be >= 0.
        source: starting node.

    Returns:
        dict mapping each reachable node to its shortest distance from source.

    Examples:
        >>> g = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
        >>> dijkstra(g, 0)
        {0: 0, 2: 1, 1: 3, 3: 4}
    """
    dist: Dict[int, float] = {source: 0.0}
    heap: List[Tuple[float, int]] = [(0.0, source)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist.get(u, float("inf")):
            continue  # stale entry
        for v, w in graph.get(u, []):
            new_dist = d + w
            if new_dist < dist.get(v, float("inf")):
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return dist


# ---------------------------------------------------------------------------
# Quick self-test
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    _graph: Graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [],
    }
    result = dijkstra(_graph, 0)
    print("Distances:", result)  # {0:0, 1:3, 2:1, 3:4}
