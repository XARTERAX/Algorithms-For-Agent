---
title: "Dijkstra's Algorithm"
id: 0003
source: "custom"
difficulty: "Medium"
topics: ["graph", "shortest-path", "heap", "weighted"]
languages: ["python"]
time_complexity: "O((V + E) log V)"
space_complexity: "O(V)"
date: 2026-04-27
---

# Problem

Given a weighted directed graph represented as an adjacency list and a source node, find the **shortest distance** from the source to every other node. Edge weights are non-negative.

**Input:**
- `graph`: `Dict[int, List[Tuple[int, int]]]` — `{node: [(neighbour, weight), ...]}`
- `source`: `int`
- `num_nodes`: `int`

**Output:** `List[float]` — `dist[i]` is the shortest distance from source to node i (`float('inf')` if unreachable).

# Examples

```
graph = {
  0: [(1, 4), (2, 1)],
  1: [(3, 1)],
  2: [(1, 2), (3, 5)],
  3: [],
}
source = 0, num_nodes = 4

Output: [0, 3, 1, 4]
  # 0→0: 0, 0→2→1: 3, 0→2: 1, 0→2→1→3: 4
```

# Brute Force

Bellman-Ford: relax all edges V−1 times — O(V·E).

# Optimized Idea (思路链)

1. **Model** — Weighted directed graph; min-heap to always process the closest unvisited node.
2. **Brute force recap** — Bellman-Ford repeats work; Dijkstra avoids it by greedily picking the minimum.
3. **Pattern** — Greedy: the node with the smallest current distance is finalized and never updated again (valid for non-negative weights).
4. **Key invariant** — When a node is popped from the heap, `dist[node]` is final.
5. **Pseudocode**

```
dist = [inf] * num_nodes; dist[source] = 0
heap = [(0, source)]

while heap:
    d, u = heappop(heap)
    if d > dist[u]: continue   # stale entry
    for v, w in graph[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            heappush(heap, (dist[v], v))
return dist
```

- Time: O((V + E) log V) · Space: O(V)

# Implementation (Python)

```python
# See implementations/python/0003_dijkstra.py
```

# Tests

| # | Input | Expected Output | Notes |
|---|-------|-----------------|-------|
| 1 | Graph from example | [0, 3, 1, 4] | happy path |
| 2 | Single node | [0] | trivial |
| 3 | Disconnected graph | inf for unreachable | disconnected |

# Recap (3 lines)

1. **Key idea:** Use a min-heap to always relax edges from the node with the current smallest tentative distance.
2. **Why correct:** With non-negative weights, once a node is popped its distance is provably optimal (greedy correctness).
3. **Complexity:** Time O((V + E) log V), Space O(V).
