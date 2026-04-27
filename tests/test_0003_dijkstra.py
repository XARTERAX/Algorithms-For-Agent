from conftest import load_impl

_m = load_impl("0003_dijkstra.py")
dijkstra = _m.dijkstra


def test_basic():
    graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }
    result = dijkstra(graph, "A")
    assert result["A"] == 0
    assert result["B"] == 1
    assert result["C"] == 3
    assert result["D"] == 4


def test_disconnected():
    graph = {"A": [], "B": []}
    result = dijkstra(graph, "A")
    assert result["A"] == 0
    assert result["B"] == float("inf")


def test_single_node():
    graph = {"X": []}
    result = dijkstra(graph, "X")
    assert result == {"X": 0}


def test_direct_edge():
    graph = {"A": [("B", 7)], "B": []}
    result = dijkstra(graph, "A")
    assert result["B"] == 7
