---
title: "Dijkstra's Algorithm"
id: 0003
source: ""
difficulty: "Medium"
topics: ["graph", "shortest-path", "pathfinding"]
languages: ["python"]
time_complexity: "O((V + E) log V)"
space_complexity: "O(V)"
date: 2024-01-01
---

# Problem

Given a weighted directed graph (as an adjacency list) and a source node, find the shortest distance from the source to every other node using Dijkstra's algorithm. Return a dict mapping node → shortest distance. Unreachable nodes map to `float("inf")`.

## Examples

**Example 1**
- Graph:
  ```
  A --(1)--> B
  A --(4)--> C
  B --(2)--> C
  B --(5)--> D
  C --(1)--> D
  ```
- Input: `graph = {"A": [("B",1),("C",4)], "B": [("C",2),("D",5)], "C": [("D",1)], "D": []}`, `source = "A"`
- Output: `{"A": 0, "B": 1, "C": 3, "D": 4}`

**Example 2 — disconnected node**
- Input: same graph, but add node `"E"` with no edges.
- Output: `{"A": 0, "B": 1, "C": 3, "D": 4, "E": inf}`

## Constraints

- No negative edge weights
- Graph may be directed or undirected
- V ≤ 10 000, E ≤ 100 000

# Approach

## Brute Force

Bellman-Ford runs in O(VE) — correct for negative weights but overkill here.

## Optimized Idea

1. Initialise `dist[source] = 0`, all others = ∞.
2. Use a min-heap `(dist, node)`; push `(0, source)`.
3. Pop the node with the smallest known distance; skip if already finalised.
4. Relax all outgoing edges.

```
dist = {node: inf for node in graph}
dist[source] = 0
heap = [(0, source)]

while heap:
    d, u = heappop(heap)
    if d > dist[u]: continue        # stale entry
    for v, weight in graph[u]:
        if dist[u] + weight < dist[v]:
            dist[v] = dist[u] + weight
            heappush(heap, (dist[v], v))
```

## Complexity Analysis

| | Time | Space |
|---|---|---|
| Bellman-Ford | O(VE) | O(V) |
| Dijkstra (heap) | O((V+E) log V) | O(V) |

# Implementation (Python)

```python
# See implementations/python/0003_dijkstra.py
```

# 3-Line Recap

1. **Key idea**: Greedily settle the unvisited node with the smallest tentative distance using a min-heap.
2. **Why it works**: Non-negative weights guarantee that once a node is popped from the heap its distance is final (no later path can be shorter).
3. **Pitfalls / edge cases**: Skip stale heap entries by checking `d > dist[u]`; initialise all nodes — including isolated ones — to ∞.
