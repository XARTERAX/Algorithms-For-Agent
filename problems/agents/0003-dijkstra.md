---
title: "Dijkstra Shortest Path"
id: 0003
source: "custom"
difficulty: "Medium"
topics: ["graph", "shortest-path", "priority-queue"]
languages: ["python"]
time_complexity: "O((V + E) log V)"
space_complexity: "O(V + E)"
date: 2026-04-27
---

# Problem

Given a weighted directed graph as an adjacency list and a source node, find the **shortest distance** from the source to every other node.  
Return a dictionary `{node: distance}`.  Nodes unreachable from the source have distance `float('inf')`.

## Examples

```
Input:
  graph = {
      0: [(1, 4), (2, 1)],   # node: [(neighbour, weight), ...]
      1: [(3, 1)],
      2: [(1, 2), (3, 5)],
      3: [],
  }
  source = 0

Output:
  {0: 0, 1: 3, 2: 1, 3: 4}
```

## Constraints

- 1 ≤ V ≤ 10⁴, 0 ≤ E ≤ 10⁵
- All edge weights ≥ 0
- No self-loops

---

# Brute Force

Relax all edges V-1 times (Bellman-Ford) — O(V · E) time.  
Works for negative weights but is slower than needed when weights are non-negative.

---

# Optimised Idea (思路链)

1. **Model:** Weighted directed graph; we want single-source shortest paths.
2. **Bottleneck in Bellman-Ford:** We relax every edge V-1 times even if most are already settled.
3. **Pattern:** Dijkstra greedily relaxes the *closest unvisited node* first via a min-heap.
4. **Key invariant:** Once a node is popped from the heap, its distance is finalized (cannot be improved later) because all edge weights are non-negative.

### Pseudocode

```
dist = {v: ∞ for all v}
dist[source] = 0
heap = [(0, source)]

while heap:
    d, u = heappop(heap)
    if d > dist[u]: continue    # stale entry
    for (v, w) in graph[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            heappush(heap, (dist[v], v))

return dist
```

---

# Implementation

```python
# See implementations/python/0003_dijkstra.py
```

---

# Tests

```python
# See tests/test_0003_dijkstra.py
```

---

# 3-Line Recap

1. **Key idea:** Process nodes in order of their current shortest-distance estimate using a min-heap; the greedy choice is safe because weights are non-negative.
2. **Complexity:** O((V + E) log V) time with a binary heap; O(V + E) space.
3. **Why correct:** Non-negative weights guarantee that when a node is settled, no future relaxation can produce a shorter path to it.
