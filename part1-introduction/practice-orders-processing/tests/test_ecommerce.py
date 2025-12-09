from src.ecommerce import Product, OrderError, process_order
from datetime import datetime
import pytest


def test_process_order():
    bananas = Product(
        name='Bananas',
        stock=10000,
        price=1,
    )
    processing_result = process_order(
        product=bananas,
        quantity=10,
        is_premium_user=False,
        order_time=datetime(2030, 7, 1)
    )
    assert processing_result['product'] == 'Bananas'
    assert processing_result['total'] == 10 * 1


def test_process_order_premium_users():
    bananas = Product(
        name='Bananas',
        stock=10000,
        price=1,
    )
    processing_result = process_order(
        product=bananas,
        quantity=10,
        is_premium_user=True,
        order_time=datetime(2030, 7, 1)
    )
    assert processing_result['product'] == 'Bananas'
    assert processing_result['total'] == (10 * 1) * 0.9


def test_process_order_not_available():
    bananas = Product(
        name='Bananas',
        stock=100,
        price=1,
    )
    with pytest.raises(OrderError):
        process_order(
            product=bananas,
            quantity=1000,
            is_premium_user=False,
            order_time=datetime(2030, 7, 1)
        )
