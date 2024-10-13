from src.product import Product
from abc import ABC, abstractmethod


class BaseEntity(ABC):
    """
    Абстрактный базовый класс для сущностей с общими свойствами name и description.
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    @abstractmethod
    def calculate_total(self):
        """
        Абстрактный метод для расчета итоговой стоимости или количества.
        """

    pass

    def __str__(self):
        return f"{self.name}: {self.description}"


class Category(BaseEntity):
    """
    Класс для представления категории товаров, наследник BaseEntity.
    """

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list = None):
        super().__init__(name, description)
        self.__products = products or []
        Category.category_count += 1
        Category.product_count += len(self.products)

    def add_product(self, product: Product):
        """
        Добавляет товар в категорию.
        Args:
            product: Объект класса Product.
        """
        if not isinstance(product, Product):
            raise TypeError(
                f"Нельзя добавить объект типа {type(product).__name__}."
                f"Ожидается объект класса Product или его наследников."
            )
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

    def calculate_total(self):
        """
        Рассчитывает общее количество товаров в категории.
        """
        return len(self.__products)

    def __str__(self):
        """
        Возвращает строковое представление объекта Category.

        """
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
