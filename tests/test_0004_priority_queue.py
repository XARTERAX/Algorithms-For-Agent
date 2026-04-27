"""Tests for PriorityQueue (0004_priority_queue.py)."""

import importlib.util
import os

import pytest

_IMPL_DIR = os.path.join(os.path.dirname(__file__), "..", "implementations", "python")
_spec = importlib.util.spec_from_file_location(
    "priority_queue", os.path.join(_IMPL_DIR, "0004_priority_queue.py")
)
_mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mod)
PriorityQueue = _mod.PriorityQueue


def test_basic_min_order():
    pq = PriorityQueue()
    pq.push("low", 3)
    pq.push("high", 1)
    pq.push("mid", 2)
    assert pq.pop() == "high"
    assert pq.pop() == "mid"
    assert pq.pop() == "low"


def test_fifo_on_equal_priority():
    pq = PriorityQueue()
    pq.push("first", 1)
    pq.push("second", 1)
    pq.push("third", 1)
    assert pq.pop() == "first"
    assert pq.pop() == "second"
    assert pq.pop() == "third"


def test_len():
    pq = PriorityQueue()
    assert len(pq) == 0
    pq.push("a", 0)
    assert len(pq) == 1
    pq.pop()
    assert len(pq) == 0


def test_bool():
    pq = PriorityQueue()
    assert not pq
    pq.push("x", 5)
    assert pq


def test_peek_does_not_remove():
    pq = PriorityQueue()
    pq.push("only", 1)
    assert pq.peek() == "only"
    assert len(pq) == 1


def test_pop_empty_raises():
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()


def test_peek_empty_raises():
    pq = PriorityQueue()
    with pytest.raises(IndexError):
        pq.peek()
