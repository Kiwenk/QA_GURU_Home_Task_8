"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from test_homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("Apple", 300, "Apple", 8000)

@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert Product.check_quantity(product, 1), ValueError('Тест провален')

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert Product.buy(product, 1), ValueError('Тест провален')

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(300000)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    def test_add_product(self, cart, product):
        cart.add_product(product, 1)
        assert cart.products[product] == 1

    def test_remove_product_none(self,cart,product):
        cart.add_product(product, 1)
        cart.remove_product(product, None)
        assert product not in cart.products

    def test_remove_product_1(self,cart,product):
        cart.add_product(product, 1)
        cart.remove_product(product, 1)
        assert product not in cart.products

    def test_remove_product_bigger_than_buy_count(self, cart, product):
        cart.add_product(product, 1000)
        cart.remove_product(product, 1)
        assert cart.products[product] == 999

    def test_clear(self,cart,product):
        cart.add_product(product, 1000)
        cart.clear()
        assert not cart.products

    def test_get_total_price_poz(self,cart,product):
        cart.add_product(product, 10000)
        assert cart.get_total_price() == 3000000.0

    def test_get_total_price_negative(self, cart, product):
        cart.add_product(product, 2323)
        assert cart.get_total_price() != 3000000.0

    def test_buy(self,cart,product):
        cart.add_product(product, 5)
        cart.buy()
        assert product.quantity == 7995
        assert not cart.products

    def test_buy_negative(self,cart,product):
        with pytest.raises(ValueError):
            cart.add_product(product, 10000)
            cart.buy()








