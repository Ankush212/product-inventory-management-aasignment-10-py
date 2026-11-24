import pytest

from inventory import (
    apply_discount,
    calculate_total_price,
    check_stock,
)


def test_calculate_total_price():
    assert calculate_total_price(500, 4) == 2000


def test_apply_discount():
    assert apply_discount(2000, 10) == 1800


def test_check_stock():
    assert check_stock(10, 5) == "Stock is available"


def test_calculate_total_price_neg():
    with pytest.raises(ValueError):
        calculate_total_price(-100, 10)


def test_invalid_disc():
    with pytest.raises(ValueError):
        apply_discount(2000, 110)


def test_neg_disc():
    with pytest.raises(ValueError):
        apply_discount(2000, -10)


def test_unavailable_stock():
    assert check_stock(10, 18) == "Stock is not available"


def test_negative_quantity():
    with pytest.raises(ValueError):
        calculate_total_price(500, -2)


def test_zero_discount():
    assert apply_discount(1000, 0) == 1000


def test_zero_stock():
    assert check_stock(0, 0) == "Stock is available"
