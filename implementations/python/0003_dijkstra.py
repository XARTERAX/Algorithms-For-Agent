"""
0003 – Dijkstra's Algorithm
=============================
Topic      : agents / pathfinding
Difficulty : Medium

Problem
-------
Given a weighted directed graph (adjacency list, non-negative weights) and a
source node, return the shortest distance from the source to every node.

Examples
--------
>>> graph = {0: [(1,4),(2,1)], 1: [(3,1)], 2: [(1,2),(3,5)], 3: []}
>>> dijkstra(graph, source=0, num_nodes=4)
[0, 3, 1, 4]

Complexity
----------
Time : O((V + E) log V)
Space: O(V)
"""

import heapq
import math
from typing import Dict, List, Tuple


def dijkstra(
    graph: Dict[int, List[Tuple[int, int]]],
    source: int,
    num_nodes: int,
) -> List[float]:
    """Return shortest distances from source to every node.

    Parameters
    ----------
    graph : Dict[int, List[Tuple[int, int]]]
        Adjacency list: {node: [(neighbour, weight), ...]}.
        All nodes in [0, num_nodes) must appear as keys.
    source : int
        Source node index.
    num_nodes : int
        Total number of nodes.

    Returns
    -------
    List[float]
        dist[i] = shortest distance from source to i (math.inf if unreachable).
    """
    dist = [math.inf] * num_nodes
    dist[source] = 0.0
    # heap entries: (distance, node)
    heap: List[Tuple[float, int]] = [(0.0, source)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist[u]:
            continue  # stale entry
        for v, w in graph.get(u, []):
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                heapq.heappush(heap, (new_dist, v))

    return dist


# ---------------------------------------------------------------------------
# Quick smoke test
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    graph = {
        0: [(1, 4), (2, 1)],
        1: [(3, 1)],
        2: [(1, 2), (3, 5)],
        3: [],
    }
    result = dijkstra(graph, source=0, num_nodes=4)
    print("Distances:", result)  # [0, 3, 1, 4]
