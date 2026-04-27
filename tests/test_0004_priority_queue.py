import pytest
from conftest import load_impl

_m = load_impl("0004_priority_queue.py")
MinPriorityQueue = _m.MinPriorityQueue


def test_order():
    pq = MinPriorityQueue()
    pq.push("low", 1)
    pq.push("high", 10)
    pq.push("mid", 5)
    assert pq.pop() == "low"
    assert pq.pop() == "mid"
    assert pq.pop() == "high"


def test_peek_does_not_remove():
    pq = MinPriorityQueue()
    pq.push("a", 3)
    assert pq.peek() == "a"
    assert len(pq) == 1


def test_is_empty():
    pq = MinPriorityQueue()
    assert pq.is_empty()
    pq.push("x", 1)
    assert not pq.is_empty()
    pq.pop()
    assert pq.is_empty()


def test_pop_empty_raises():
    pq = MinPriorityQueue()
    with pytest.raises(IndexError):
        pq.pop()


def test_equal_priorities_stable():
    pq = MinPriorityQueue()
    pq.push("first", 1)
    pq.push("second", 1)
    # Both have priority 1; insertion order determines output (counter tiebreak)
    assert pq.pop() == "first"
    assert pq.pop() == "second"
