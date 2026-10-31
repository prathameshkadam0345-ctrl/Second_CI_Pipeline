import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "code")
)

import importlib

module = importlib.import_module("38_missing_number_xor")


def test_missing_number_middle():
    assert module.find_missing_number([1, 2, 4, 5]) == 3


def test_missing_number_first():
    assert module.find_missing_number([2, 3, 4, 5]) == 1


def test_missing_number_last():
    assert module.find_missing_number([1, 2, 3, 4]) == 5


def test_missing_number_small_list():
    assert module.find_missing_number([2]) == 1
    