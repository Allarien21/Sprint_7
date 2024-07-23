import pytest
import allure
import data
import request
import helpers


@allure.suite('Тесты на создание курьера')
class TestCreateCourier:
    @allure.title('Создание курьера')
    @allure.description('Тест на создание курьера и проверка ответа')
    def test_create_courier(self, courier_credentials):
        create_response = request.create_courier(courier_credentials)

        assert create_response.status_code == 201
        assert create_response.json() == {'ok': True}



    @allure.title('Тет на создание дубликата курьера')
    @allure.description('Создание двух одинаковых курьеров')
    def test_create_duplicated_courier(self, courier_credentials):
        create_response = request.create_courier(courier_credentials)
        assert create_response.status_code == 201

        create_response2 = request.create_courier(courier_credentials)
        assert create_response2.status_code == 409
        assert "message" in create_response2.json()
        assert create_response2.json()["message"] == data.ERROR_CREATE_COURIER_DUPLICATION



    @allure.title('Тест на проверку с пустым обязательным полем')
    @allure.description('Создание курьера с пустым логином и паролем')
    @pytest.mark.parametrize('empty_field', ['login', 'password'])
    def test_create_courier_with_empty_fields(self,empty_field):
        credentials = helpers.generate_new_courier_credentials(empty_field=empty_field)
        create_response = request.create_courier(credentials)

        assert create_response.status_code == 400
        assert "message" in create_response.json()
        assert create_response.json()["message"] == data.MESSAGE_BAD_REQUEST



    @allure.title('Тест на проверку с пропущеным полем')
    @allure.description('Создание курьера с пустым именем')
    def test_create_courier_with_missing_field(self, courier_credentials):
        courier_credentials['firstName'] = ''
        create_response = request.create_courier(courier_credentials)

        assert create_response.status_code == 201
        assert create_response.json() == {'ok': True}