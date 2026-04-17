"""
Unit tests for the calculator module.

Naming conventions followed:
  - Test file: test_<module>.py
  - Test function: test_<behaviour>_<condition>()
  - One assertion per test where possible (single responsibility)
"""

import pytest
from calculator import add, subtract, multiply, divide, power, is_even


# ─── Tests for add() ─────────────────────────────────────────────

def test_add_two_positive_integers():
    assert add(2, 3) == 5


def test_add_positive_and_negative():
    assert add(10, -3) == 7


def test_add_two_floats():
    assert add(1.5, 2.5) == 4.0


def test_add_zero():
    assert add(7, 0) == 7


# ─── Tests for subtract() ────────────────────────────────────────

def test_subtract_positive_result():
    assert subtract(10, 4) == 6


def test_subtract_negative_result():
    assert subtract(3, 10) == -7


# ─── Tests for multiply() ────────────────────────────────────────

def test_multiply_two_integers():
    assert multiply(4, 5) == 20


def test_multiply_by_zero():
    assert multiply(99, 0) == 0


def test_multiply_negative_numbers():
    assert multiply(-3, -4) == 12


# ─── Tests for divide() ──────────────────────────────────────────

def test_divide_even_division():
    assert divide(10, 2) == 5.0


def test_divide_float_result():
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises_value_error():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)


# ─── Tests for power() ──────────────────────────────────────────

def test_power_positive_exponent():
    assert power(2, 8) == 256


def test_power_zero_exponent():
    assert power(99, 0) == 1


# ─── Tests for is_even() ─────────────────────────────────────────

def test_is_even_with_even_number():
    assert is_even(4) is True


def test_is_even_with_odd_number():
    assert is_even(7) is False


def test_is_even_with_zero():
    assert is_even(0) is True