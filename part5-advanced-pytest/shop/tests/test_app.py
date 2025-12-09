import pytest

from src.app import discount


def test_discount_for_vip_user():
    assert discount(100.0, "vip") == pytest.approx(80.0)


def test_discount_for_regular_user():
    assert discount(100.0, "regular") == pytest.approx(90.0)


def test_discount_for_new_user():
    assert discount(100.0, "new") == pytest.approx(100.0)
