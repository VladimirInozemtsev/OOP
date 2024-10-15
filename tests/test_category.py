import unittest
from unittest.mock import patch
from src.category import Category, CategoryIterator
from src.product import Product, Smartphone, LawnGrass


class TestCategory(unittest.TestCase):

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

    def test_smartphone_init(self):
        smartphone = Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5, "95.5", "S23 Ultra", 256, "Серый"
        )
        self.assertEqual(smartphone.name, "Samsung Galaxy S23 Ultra")
        self.assertEqual(smartphone.description, "256GB, Серый цвет")
        self.assertEqual(smartphone.price, 180000.0)
        self.assertEqual(smartphone.quantity, 5)
        self.assertEqual(smartphone.efficiency, "95.5")
        self.assertEqual(smartphone.model, "S23 Ultra")
        self.assertEqual(smartphone.memory, 256)
        self.assertEqual(smartphone.color, "Серый")

    def test_lawngrass_init(self):
        grass = LawnGrass("Газонная трава", "Элитная трава", 500.0, 20, "Россия", 7, "Зеленый")
        self.assertEqual(grass.name, "Газонная трава")
        self.assertEqual(grass.description, "Элитная трава")
        self.assertEqual(grass.price, 500.0)
        self.assertEqual(grass.quantity, 20)
        self.assertEqual(grass.country, "Россия")
        self.assertEqual(grass.germination_period, 7)
        self.assertEqual(grass.color, "Зеленый")

    def test_add_same_type(self):
        smartphone1 = Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5, "95.5", "S23 Ultra", 256, "Серый"
        )
        smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, "98.2", "15", 512, "Gray space")
        result = smartphone1 + smartphone2
        self.assertEqual(result, smartphone1.price * smartphone1.quantity + smartphone2.price * smartphone2.quantity)

    def test_add_different_type(self):
        smartphone = Smartphone(
            "Samsung Galaxy S23 Ultra", "256GB, Серый цвет", 180000.0, 5, "95.5", "S23 Ultra", 256, "Серый"
        )
        grass = LawnGrass("Газонная трава", "Элитная трава", 500.0, 20, "Россия", "7", "Зеленый")
        with self.assertRaises(TypeError):
            result = smartphone + grass


class TestCategoryIterator(unittest.TestCase):

    def test_iterator(self):
        product1 = Product("Product 1", "Description 1", 1500.0, 5)
        product2 = Product("Product 2", "Description 2", 3000.0, 3)
        category = Category("Electronics", "Категория электроники", [product1, product2])

        iterator = CategoryIterator(category)
        products = list(iterator)

        self.assertEqual(products[0], "Product 1, 1500.0 руб. Остаток: 5 шт.")
        self.assertEqual(products[1], "Product 2, 3000.0 руб. Остаток: 3 шт.")


if __name__ == "__main__":
    unittest.main()
