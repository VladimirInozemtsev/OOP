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

    def __str__(self):
        """
        Возвращает строковое представление объекта Product.
        """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Сложение товаров: возвращает сумму стоимости товаров на складе.

        Args:
            other: Любой объект Product.

        Returns:
            Сумма стоимости товаров (float).
        """
        if not isinstance(other, Product):
            raise TypeError("Складывать можно только объекты Product.")

        if type(self) is not type(other):
            raise TypeError(f"Нельзя сложить объекты разных типов: {type(self).__name__} и {type(other).__name__}.")

        return self.price * self.quantity + other.price * other.quantity


class Smartphone(Product):
    """
    Класс для представления смартфона.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int, efficiency: str, model: str,
                 memory: int, color: str):
        """
        Инициализация объекта смартфона.

        Args:
            name: Название товара.
            description: Описание товара.
            price: Цена товара.
            quantity: Количество товара в наличии.
            efficiency: Производительность смартфона.
            model: Модель смартфона.
            memory: Объем встроенной памяти смартфона.
            color: Цвет смартфона.
        """
        super().__init__(name, description, price, quantity)  # Наследуем общие свойства от Product
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __str__(self):
        """
        Возвращает строковое представление объекта Smartphone.
        """
        return (f"{self.name} (Модель: {self.model}, Память: {self.memory}GB, "
                f"Производительность: {self.efficiency}, Цвет: {self.color}), "
                f"{self.price} руб. Остаток: {self.quantity} шт.")


class LawnGrass(Product):
    """
    Класс для представления газонной травы.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int, country: str, germination_period: str,
                 color: str):
        """
        Инициализация объекта газонной травы.

        Args:
            name: Название товара.
            description: Описание товара.
            price: Цена товара.
            quantity: Количество товара в наличии.
            country: Страна-производитель.
            germination_period: Срок прорастания в днях.
            color: Цвет травы.
        """
        super().__init__(name, description, price, quantity)  # Наследуем общие свойства от Product
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __str__(self):
        """
        Возвращает строковое представление объекта LawnGrass.
        """
        return (f"{self.name} (Производство: {self.country}, Срок прорастания: {self.germination_period} дней, "
                f"Цвет: {self.color}), {self.price} руб. Остаток: {self.quantity} шт.")