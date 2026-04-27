---
title: "Dijkstra Shortest Path"
id: 0003
source: "classic"
difficulty: "Medium"
topics: ["agent", "graph", "shortest-path"]
languages: ["python"]
time_complexity: "O((V + E) log V)"
space_complexity: "O(V + E)"
date: 2026-04-27
---

# Problem

Given a weighted graph (adjacency list) with non-negative edge weights, find
the shortest-distance from a `source` node to all other nodes using
**Dijkstra's algorithm**.

**Input:**
- `graph`: `dict[node, list[(neighbour, weight)]]`
- `source`: starting node

**Output:** `dict[node, float]` — shortest distance from source to every node
(unreachable nodes map to `inf`).

# Examples

**Example 1:**
```
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': [],
}
source = 'A'
Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}
```

**Example 2 (disconnected node):**
```
graph = {'A': [], 'B': []}
source = 'A'
Output: {'A': 0, 'B': inf}
```

# Brute Force

Relax all edges V-1 times (Bellman-Ford) — O(VE); correct but slower when
weights are non-negative.

# Optimized Idea

1. **Model** — weighted directed graph; find minimum-cost path.
2. **Bottleneck** — iterating all edges for each relaxation is O(VE).
3. **Pattern** — greedy: always expand the cheapest unvisited node via a
   min-heap; safe because all weights are non-negative.
4. **Invariant** — when a node is popped its distance is final.
5. **Complexity** — O((V + E) log V) with a binary heap.

# Pseudocode

```
dist = {node: inf for node in graph};  dist[source] = 0
heap = [(0, source)]
visited = set()

while heap:
    d, u = heappop(heap)
    if u in visited: continue
    visited.add(u)
    for v, w in graph[u]:
        if d + w < dist[v]:
            dist[v] = d + w
            heappush(heap, (dist[v], v))

return dist
```

# Implementation

```python
# See implementations/python/0003_dijkstra.py
```

# Tests

```python
# See tests/test_0003_dijkstra.py
```

# Notes

> **Key idea:** Greedy expansion of the cheapest frontier node is correct when
> all edge weights are non-negative — proven by the "shortest-path tree"
> optimality condition.  
> **Complexity:** Time O((V+E) log V), Space O(V+E).  
> **Next improvements:** use Fibonacci heap for O(V log V + E); add
> Bellman-Ford variant for negative weights.
