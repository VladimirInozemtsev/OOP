import pytest
from src.order import Order
from src.product import Product

class TestOrder:

    def test_order_creation(self, order, product):
        assert order.name == "Order #1"
        assert order.product == product
        assert order.quantity == 3
        assert order.total_price == 4500.0

    def test_order_total_price(self, order):
        assert order.calculate_total() == 4500.0
