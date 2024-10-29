import pytest
from src.exception import InvalidQuantityError
from src.product import Product
from src.category import Category


def test_product_zero_quantity():
    """
    Тест создания продукта с нулевым количеством
    """
    with pytest.raises(InvalidQuantityError) as exc_info:
        Product("Test Product", "Description", 100.0, 0)
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"


def test_product_negative_quantity():
    """
    Тест создания продукта с отрицательным количеством
    """
    with pytest.raises(InvalidQuantityError) as exc_info:
        Product("Test Product", "Description", 100.0, -5)
    assert str(exc_info.value) == "Товар с нулевым количеством не может быть добавлен"


def test_category_add_zero_quantity_product(capsys):
    """
    Тест добавления продукта с нулевым количеством в категорию
    """
    category = Category("Test Category", "Description")
    product = Product("Test Product", "Description", 100.0, 1)
    product.quantity = 0  # Принудительно устанавливаем количество в 0 после создания
    category.add_product(product)

    captured = capsys.readouterr()
    assert captured.out


def test_category_average_price_empty():
    """
    Тест подсчета средней цены для пустой категории
    """
    category = Category("Test Category", "Description")
    assert category.average_price() == 0


def test_category_average_price_with_products():
    """
    Тест подсчета средней цены для категории с товарами
    """
    category = Category("Test Category", "Description")
    product1 = Product("Product 1", "Description", 100.0, 1)
    product2 = Product("Product 2", "Description", 200.0, 1)
    category.add_product(product1)
    category.add_product(product2)
    assert category.average_price() == 150.0