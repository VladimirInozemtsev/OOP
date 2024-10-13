import unittest
from unittest.mock import patch
from src.category import Product, Category, CategoryIterator


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
        self.assertCountEqual(
            category.products, ["Товар 1, 100.5 руб. Остаток: 5 шт.", "Товар 2, 50.0 руб. Остаток: 10 шт."]
        )

    def test_category_count_products(self):
        product1 = Product("Товар 1", "Описание товара 1", 100.50, 5)
        product2 = Product("Товар 2", "Описание товара 2", 50.00, 10)
        category = Category("Категория 1", "Описание категории 1", [product1, product2])
        self.assertEqual(len(category.products), 2)
        self.assertEqual(Category.product_count, 3)

    def test_category_count_categories(self):
        category1 = Category("Категория 1", "Описание категории 1")
        category2 = Category("Категория 2", "Описание категории 2")
        self.assertEqual(Category.category_count, 3)

    def test_category_add_product(self):
        category = Category("Категория 1", "Описание категории 1")
        product1 = Product("Товар 1", "Описание товара 1", 100.50, 5)
        category.add_product(product1)
        self.assertEqual(len(category.products), 1)
        self.assertEqual(Category.product_count, 1)

    def test_product_new_product_no_duplicates(self):
        product_data = {"name": "Товар 1", "description": "Описание товара 1", "price": 100.0, "quantity": 5}
        product = Product.new_product(product_data)
        self.assertEqual(product.name, "Товар 1")
        self.assertEqual(product.description, "Описание товара 1")
        self.assertEqual(product.price, 100.0)
        self.assertEqual(product.quantity, 5)

    def test_product_new_product_with_duplicates(self):
        product_data1 = {"name": "Товар 1", "description": "Описание товара 1", "price": 100.0, "quantity": 5}
        product_data2 = {"name": "Товар 1", "description": "Описание товара 1", "price": 120.0, "quantity": 3}

        existing_product = Product("Товар 1", "Описание", 90.0, 3)
        existing_products = [existing_product]

        new_product = Product.new_product(product_data1, existing_products)
        self.assertEqual(new_product.price, 100.0)
        self.assertEqual(new_product.quantity, 8)
        self.assertEqual(new_product, existing_product)

    @patch("builtins.input", return_value="y")
    def test_product_price_setter_decrease_price_confirmation(self, mock_input):
        product = Product("Товар 1", "Описание", 100.0, 5)
        product.price = 80.0
        self.assertEqual(product.price, 80.0)
        mock_input.assert_called_once_with("Подтвердите понижение цены с 100.0 до 80.0 (y/n): ")

    @patch("builtins.input", return_value="n")
    def test_product_price_setter_decrease_price_cancel(self, mock_input):
        product = Product("Товар 1", "Описание", 100.0, 5)
        product.price = 80.0
        self.assertEqual(product.price, 100.0)
        mock_input.assert_called_once_with("Подтвердите понижение цены с 100.0 до 80.0 (y/n): ")

    def test_product_price_setter_valid_price(self):
        product = Product("Товар 1", "Описание", 100.0, 5)
        product.price = 120.0
        self.assertEqual(product.price, 120.0)

    def test_product_price_setter_invalid_price(self):
        product = Product("Товар 1", "Описание", 100.0, 5)
        product.price = 0.0
        self.assertEqual(product.price, 100.0)


class TestCategoryIterator(unittest.TestCase):

    def test_iterator(self):
        category = Category("Категория 1", "Описание категории 1")
        product1 = Product("Товар 1", "Описание 1", 100.0, 10)
        product2 = Product("Товар 2", "Описание 2", 200.0, 5)
        category.add_product(product1)
        category.add_product(product2)

        iterator = CategoryIterator(category)
        self.assertEqual(str(next(iterator)), str(product1))
        self.assertEqual(str(next(iterator)), str(product2))
        with self.assertRaises(StopIteration):
            next(iterator)


if __name__ == "__main__":
    unittest.main()
