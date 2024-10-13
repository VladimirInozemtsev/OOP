from src.product import Product


class Category:
    """
    Класс для представления категории товаров.
    """

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        """
        Инициализация объекта категории.

        Args:
            name: Название категории.
            description: Описание категории.

        """
        self.name = name
        self.description = description
        self.__products = products or []
        Category.category_count += 1
        Category.product_count += len(self.products)

    def add_product(self, product: Product):
        """
        Добавляет товар в категорию.
        Args:
            product: Объект класса Product.
        """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """
        Геттер для вывода списка товаров в виде строк.
        """
        product_strings = []
        for product in self.__products:
            product_strings.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return product_strings

    def __str__(self):
        """
        Возвращает строковое представление объекта Category.

        """
        #products_str = "\n".join(f"  - {product}" for product in self.__products)
        return f"{self.name}, количество продуктов: {len(self.__products)} шт."


class CategoryIterator:
    """
    Итератор для перебора товаров в категории.
    """

    def __init__(self, category: Category):
        """
        Инициализация итератора.

        Args:
            category: Объект класса Category.
        """
        self.category = category
        self.index = 0

    def __iter__(self):
        """
        Возвращает сам итератор.
        """
        return self

    def __next__(self):
        """
        Возвращает следующий товар из категории.

        Returns:
            Объект класса Product.
        """
        if self.index < len(self.category.products):
            product = self.category.products[self.index]
            self.index += 1
            return product
        else:
            raise StopIteration


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(str(product1))
    print(str(product2))
    print(str(product3))

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(str(category1))

    print(category1.products)

    print(product1 + product2)
    print(product1 + product3)
    print(product2 + product3)

    for product in CategoryIterator(category1):
        print(product)
