from src.product import Product
from src.category import BaseEntity

class Order(BaseEntity):
    """
    Класс для представления заказа, наследник BaseEntity.
    """

    def __init__(self, name: str, description: str, product: Product, quantity: int):
        """
        Инициализация объекта заказа.

        Args:
            name: Название заказа.
            description: Описание заказа.
            product: Объект класса Product.
            quantity: Количество товара в заказе.
        """
        super().__init__(name, description)
        self.product = product
        self.quantity = quantity
        self.total_price = self.calculate_total()

    def calculate_total(self):
        """
        Рассчитывает общую стоимость заказа на основе количества и цены товара.
        """
        return self.product.price * self.quantity

    def __str__(self):
        return (f"Заказ: {self.name}, Товар: {self.product.name}, "
                f"Количество: {self.quantity}, Общая стоимость: {self.total_price} руб.")