import pytest
import allure
import request
from faker import Faker

from helpers import Order

fake = Faker()

@allure.suite('Тесты создания заказа')
class TestCreateOrders:
    @allure.title('Успешное создание заказа')
    @allure.description('Генерация данных для заказа и проверка ответа')
    @pytest.mark.parametrize("color", [["BLACK"], ["GREY"],["BLACK","GREY"], []])
    def test_create_order(self,color):
        new_order = Order(
            firstName=fake.first_name(),
            lastName=fake.last_name(),
            address=fake.address(),
            metroStation=4,
            phone=fake.phone_number(),
            rentTime=5,
            deliveryDate=fake.date(),
            comment="Call in 10 minutes",
            color=color
        )
        response = request.create_order(new_order)
        assert response.status_code == 201
        assert "track" in response.json()
