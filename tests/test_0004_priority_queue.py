import importlib.util
import os
import pytest

_impl_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "implementations",
    "python",
    "0004_priority_queue.py",
)
_spec = importlib.util.spec_from_file_location("priority_queue", _impl_path)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
PriorityQueue = _mod.PriorityQueue


def test_pop_order():
    pq = PriorityQueue()
    pq.push("node_B", 3)
    pq.push("node_A", 1)
    pq.push("node_C", 2)
    assert pq.pop() == "node_A"
    assert pq.pop() == "node_C"
    assert pq.pop() == "node_B"


def test_is_empty():
    pq = PriorityQueue()
    assert pq.is_empty()
    pq.push("x", 0)
    assert not pq.is_empty()
    pq.pop()
    assert pq.is_empty()


def test_peek_does_not_remove():
    pq = PriorityQueue()
    pq.push("a", 5)
    pq.push("b", 1)
    assert pq.peek() == "b"
    assert len(pq) == 2


def test_push_after_pop():
    pq = PriorityQueue()
    pq.push("first", 10)
    pq.pop()
    pq.push("second", 1)
    assert pq.pop() == "second"


def test_pop_empty_raises():
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()


def test_peek_empty_raises():
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.peek()
