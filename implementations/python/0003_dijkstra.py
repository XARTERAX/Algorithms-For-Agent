"""
Problem ID: 0003
Title: Dijkstra Shortest Path
Difficulty: Medium
Topics: graph, shortest-path, agent

Single-source shortest path on a weighted directed graph.
"""
import heapq
from typing import Any


def dijkstra(
    graph: dict[Any, list[tuple[Any, float]]],
    source: Any,
    target: Any,
) -> tuple[float, list[Any]]:
    """
    Dijkstra's algorithm for shortest path.

    Args:
        graph:  Adjacency list {node: [(neighbour, weight), ...]}.
                All weights must be non-negative.
        source: Starting node.
        target: Destination node.

    Returns:
        (distance, path) where path is the ordered list of nodes,
        or (float('inf'), []) if target is unreachable.

    Time:  O((V + E) log V)
    Space: O(V)
    """
    dist: dict[Any, float] = {source: 0.0}
    parent: dict[Any, Any] = {source: None}
    heap: list[tuple[float, Any]] = [(0.0, source)]

    while heap:
        d, u = heapq.heappop(heap)
        if d > dist.get(u, float("inf")):
            continue  # stale entry
        if u == target:
            path: list[Any] = []
            node = target
            while node is not None:
                path.append(node)
                node = parent[node]
            path.reverse()
            return dist[target], path

        for v, w in graph.get(u, []):
            new_dist = dist[u] + w
            if new_dist < dist.get(v, float("inf")):
                dist[v] = new_dist
                parent[v] = u
                heapq.heappush(heap, (new_dist, v))

    return float("inf"), []


if __name__ == "__main__":
    demo_graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("D", 2)],
        "C": [("D", 1)],
        "D": [],
    }
    print(dijkstra(demo_graph, "A", "D"))
    # Expected: (3, ['A', 'B', 'D'])
