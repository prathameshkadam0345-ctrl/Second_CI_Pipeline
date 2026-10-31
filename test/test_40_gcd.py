import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "code")
)

import importlib

module = importlib.import_module("40_gcd")


def test_gcd_normal_numbers():
    assert module.gcd(12, 18) == 6


def test_gcd_coprime_numbers():
    assert module.gcd(7, 13) == 1


def test_gcd_one_number_zero():
    assert module.gcd(10, 0) == 10


def test_gcd_equal_numbers():
    assert module.gcd(8, 8) == 8