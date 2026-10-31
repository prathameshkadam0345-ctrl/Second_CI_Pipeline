import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "code")
)

import importlib

module = importlib.import_module("36_most_frequent")


def test_most_frequent_normal():
    assert module.most_frequent([1, 2, 2, 3, 2, 4]) == 2


def test_most_frequent_single_element():
    assert module.most_frequent([5]) == 5


def test_most_frequent_empty_list():
    assert module.most_frequent([]) is None


def test_most_frequent_repeated_elements():
    assert module.most_frequent([7, 7, 7, 2, 2]) == 7