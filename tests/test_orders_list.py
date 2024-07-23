import allure
import request


@allure.suite('Тесты получения списка заказов')
class TestGetOrders:
    @allure.title('Тест на получение списка всех заказов')
    @allure.description('Вызов запроса на получения списка всех заказов')
    def test_get_all_orders(self):
        response = request.get_orders()

        assert response.status_code == 200
        assert "orders" in response.json()