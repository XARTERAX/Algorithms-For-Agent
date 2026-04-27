"""
Problem: Dijkstra Shortest Path
ID: 0003
Difficulty: Medium
Topics: agent, graph, shortest-path

Find the shortest-distance from a source node to all other nodes in a weighted
directed graph with non-negative edge weights.

Function signature:
    dijkstra(graph, source) -> dict[node, float]
"""

import heapq
import math
from typing import Dict, List, Tuple

Node = str
Graph = Dict[Node, List[Tuple[Node, float]]]


def dijkstra(graph: Graph, source: Node) -> Dict[Node, float]:
    """
    Dijkstra's algorithm on a weighted directed graph.

    Parameters
    ----------
    graph  : adjacency list — {node: [(neighbour, weight), ...]}.
             All weights must be non-negative.
    source : starting node.

    Returns
    -------
    dict mapping each node to its shortest distance from source.
    Unreachable nodes map to math.inf.
    """
    dist: Dict[Node, float] = {node: math.inf for node in graph}
    dist[source] = 0.0

    # heap entries: (distance, node)
    heap: list = [(0.0, source)]
    visited: set = set()

    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)

        for v, w in graph.get(u, []):
            nd = d + w
            if nd < dist.get(v, math.inf):
                dist[v] = nd
                heapq.heappush(heap, (nd, v))

    return dist
