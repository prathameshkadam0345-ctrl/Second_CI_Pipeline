import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "code")
)

import importlib

module = importlib.import_module("39_transpose_matrix")


def test_transpose_rectangular_matrix():
    assert module.transpose_matrix([
        [1, 2, 3],
        [4, 5, 6]
    ]) == [
        [1, 4],
        [2, 5],
        [3, 6]
    ]


def test_transpose_square_matrix():
    assert module.transpose_matrix([
        [1, 2],
        [3, 4]
    ]) == [
        [1, 3],
        [2, 4]
    ]


def test_transpose_single_element():
    assert module.transpose_matrix([[5]]) == [[5]]


def test_transpose_empty_matrix():
    assert module.transpose_matrix([]) == []