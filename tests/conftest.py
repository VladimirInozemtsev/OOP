import pytest
from src.product import Product, Smartphone, LawnGrass
from src.category import Category
from src.order import Order

# Фикстура для продукта
@pytest.fixture
def product():
    return Product("Test Product", "Test Description", 1500.0, 10)

# Фикстура для смартфона
@pytest.fixture
def smartphone():
    return Smartphone("iPhone", "256GB, Черный", 120000.0, 5, "Высокая", "iPhone 13", 256, "Черный")

# Фикстура для газонной травы
@pytest.fixture
def lawn_grass():
    return LawnGrass("Газонная трава", "Элитная трава", 500.0, 20, "Россия", 7, "Зеленый")

# Фикстура для первого продукта в категории
@pytest.fixture
def product1():
    return Product("Product 1", "Description 1", 1500.0, 5)

# Фикстура для второго продукта в категории
@pytest.fixture
def product2():
    return Product("Product 2", "Description 2", 3000.0, 3)

# Фикстура для категории
@pytest.fixture
def category(product1, product2):
    return Category("Electronics", "Категория электроники", [product1, product2])

# Фикстура для заказа
@pytest.fixture
def order(product):
    return Order("Order #1", "Покупка товара", product, 3)
