class Product:
    """
    Класс для представления товара.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация объекта товара.

        Args:
            name: Название товара.
            description: Описание товара.
            price: Цена товара.
            quantity: Количество товара в наличии.
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self):
        """
        Геттер для получения цены товара.
        """
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """
        Сеттер для изменения цены товара
        Args:
             new_price: Новая цена товара.
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if new_price < self.__price:
            confirmation = input(f"Подтвердите понижение цены с {self.__price} до {new_price} (y/n): ").lower()
            if confirmation != "y":
                print("Понижение цены отменено.")
                return
        self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict, existing_products: list = None):
        """
        Создает новый объект Product из словаря данных.
        Args:
             product_data: Словарь с данными о товаре.
             existing_products: Список существующих товаров (для проверки дубликатов).
        Returns:
            Объект класса Product.
        """
        name = product_data.get("name")
        description = product_data.get("description")
        price = product_data.get("price")
        quantity = product_data.get("quantity")

        if existing_products:
            for existing_product in existing_products:
                if existing_product.name.lower() == name.lower():
                    existing_product.quantity += quantity
                    existing_product.price = max(existing_product.price, price)
                    return existing_product

        return cls(name, description, price, quantity)


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
        product_strigs = []
        for product in self.__products:
            product_strigs.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return product_strigs


if __name__ == "__main__":

    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.products)
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)

    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
