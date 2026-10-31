import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "code")
)

import importlib

module = importlib.import_module("35_move_zeros")


def test_move_zeros_normal():
    assert module.move_zeros([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]


def test_move_zeros_all_zeros():
    assert module.move_zeros([0, 0, 0]) == [0, 0, 0]


def test_move_zeros_no_zeros():
    assert module.move_zeros([1, 2, 3]) == [1, 2, 3]


def test_move_zeros_empty_list():
    assert module.move_zeros([]) == []