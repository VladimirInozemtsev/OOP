import unittest
from src.category import Product, Category


class TestProductCategory(unittest.TestCase):

    def test_product_init(self):
        product = Product("Товар 1", "Описание товара 1", 100.50, 5)
        self.assertEqual(product.name, "Товар 1")
        self.assertEqual(product.description, "Описание товара 1")
        self.assertEqual(product.price, 100.50)
        self.assertEqual(product.quantity, 5)

    def test_category_init(self):
        product1 = Product("Товар 1", "Описание товара 1", 100.50, 5)
        product2 = Product("Товар 2", "Описание товара 2", 50.00, 10)
        category = Category("Категория 1", "Описание категории 1", [product1, product2])
        self.assertEqual(category.name, "Категория 1")
        self.assertEqual(category.description, "Описание категории 1")
        self.assertEqual(category.products, [product1, product2])

    def test_category_count_products(self):
        product1 = Product("Товар 1", "Описание товара 1", 100.50, 5)
        product2 = Product("Товар 2", "Описание товара 2", 50.00, 10)
        category = Category("Категория 1", "Описание категории 1", [product1, product2])
        self.assertEqual(len(category.products), 2)
        self.assertEqual(Category.product_count, 2)

    def test_category_count_categories(self):
        category1 = Category("Категория 1", "Описание категории 1", [])
        category2 = Category("Категория 2", "Описание категории 2", [])
        self.assertEqual(Category.category_count, 2)


if __name__ == "__main__":
    unittest.main()
