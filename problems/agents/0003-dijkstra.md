---
title: "Dijkstra Shortest Path"
id: 0003
source: "classic graph"
difficulty: "Medium"
topics: ["graph", "shortest-path", "agent"]
languages: ["python"]
time_complexity: "O((V + E) log V)"
space_complexity: "O(V)"
date: 2026-04-27
---

# Problem

Given a weighted directed graph represented as an adjacency list, find the shortest-distance path from `source` to `target`.

Graph format: `{node: [(neighbour, weight), ...]}`.

Return `(distance, path)` where `path` is a list of nodes, or `(inf, [])` if unreachable.

# Examples

```
Graph:
  A --(1)--> B --(2)--> D
  A --(4)--> C --(1)--> D

Input:  source='A', target='D'
Output: (3, ['A', 'B', 'D'])

Input:  source='B', target='C'  # no path
Output: (inf, [])
```

# Brute Force

Explore all paths from source by DFS, track minimum cost — exponential in the number of edges.

# Optimized Idea (思路链)

1. **Model** — weighted directed graph; each edge has a non-negative cost.
2. **Bottleneck** — naïve approach re-explores expensive paths.
3. **Pattern** — Dijkstra: always expand the currently cheapest unvisited node.
4. **Invariant** — once a node is popped from the min-heap, its distance is final.
5. **Pseudocode**:

```
dist = {source: 0}
heap = [(0, source)]
parent = {source: None}
while heap:
    d, u = heappop(heap)
    if d > dist[u]: continue   # stale entry
    if u == target: return reconstruct(parent, target)
    for (v, w) in graph[u]:
        if dist[u] + w < dist.get(v, inf):
            dist[v] = dist[u] + w
            parent[v] = u
            heappush(heap, (dist[v], v))
return (inf, [])
```

# Implementation

See `implementations/python/0003_dijkstra.py`.

# Tests

- Simple two-path graph — picks cheapest.
- Unreachable target.
- Source equals target.
- Graph with single node.

# Review (fill in after solving)

- **Key idea**: Greedy node expansion by cost; lazy deletion handles stale heap entries.
- **Complexity**: time O((V+E) log V) | space O(V)
- **Improvement**: Use a Fibonacci heap for O(E + V log V); use bidirectional Dijkstra for large sparse graphs.
