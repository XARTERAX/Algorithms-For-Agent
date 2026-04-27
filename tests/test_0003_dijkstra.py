import importlib.util
import os
import math

_impl_path = os.path.join(
    os.path.dirname(__file__), "..", "implementations", "python", "0003_dijkstra.py"
)
_spec = importlib.util.spec_from_file_location("dijkstra", _impl_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
dijkstra = _mod.dijkstra

GRAPH = {
    "A": [("B", 1), ("C", 4)],
    "B": [("D", 2)],
    "C": [("D", 1)],
    "D": [],
}


def test_shortest_path():
    dist, path = dijkstra(GRAPH, "A", "D")
    assert dist == 3
    assert path == ["A", "B", "D"]


def test_no_path():
    dist, path = dijkstra(GRAPH, "B", "C")
    assert math.isinf(dist)
    assert path == []


def test_source_equals_target():
    dist, path = dijkstra(GRAPH, "A", "A")
    assert dist == 0
    assert path == ["A"]


def test_direct_edge():
    dist, path = dijkstra(GRAPH, "A", "B")
    assert dist == 1
    assert path == ["A", "B"]


def test_single_node_graph():
    g = {"X": []}
    dist, path = dijkstra(g, "X", "X")
    assert dist == 0
    assert path == ["X"]
