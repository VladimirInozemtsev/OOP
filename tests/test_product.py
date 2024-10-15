from unittest.mock import patch
import unittest
from src.product import Product
import pytest
from src.product import Product, Smartphone, LawnGrass


class TestReprMixin(unittest.TestCase):

    @patch("builtins.print")
    def test_mixin_creation(self, mock_print):
        product = Product("Test Product", "Test Description", 1500.0, 10)
        mock_print.assert_called_with(
            "Создан объект класса Product с параметрами: ('Test Product', 'Test Description', 1500.0, 10), {}"
        )


class TestProduct:

    def test_product_creation(self, product):  # Используем фикстуру product
        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.price == 1500.0
        assert product.quantity == 10

    def test_smartphone_creation(self, smartphone):  # Используем фикстуру smartphone
        assert smartphone.name == "iPhone"
        assert smartphone.price == 120000.0
        assert smartphone.efficiency == "Высокая"
        assert smartphone.model == "iPhone 13"
        assert smartphone.memory == 256
        assert smartphone.color == "Черный"

    def test_lawn_grass_creation(self, lawn_grass):  # Используем фикстуру lawn_grass
        assert lawn_grass.name == "Газонная трава"
        assert lawn_grass.price == 500.0
        assert lawn_grass.country == "Россия"
        assert lawn_grass.germination_period == 7
        assert lawn_grass.color == "Зеленый"

    def test_product_price_setter(self, product):
        product.price = 2000.0
        assert product.price == 2000.0
