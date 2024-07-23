import data
import request
import allure
import helpers


@allure.suite('Тесты логина курьера')
class TestLoginCourier:
    @allure.title('Успешная авторизация курьера')
    @allure.description('Тест на проверку логина курьера')
    def test_courier_login_successful(self, created_courier_credentials):
        login_data = helpers.create_login(created_courier_credentials)
        login_response = request.login_courier(login_data)

        assert login_response.status_code == 200
        assert "id" in login_response.json()

    @allure.title('Невалидные креды (логин)')
    @allure.description('Тест авторизации при не верном пароле')
    def test_courier_login_with_incorrect_login(self, created_courier_credentials):
        login_data = helpers.create_login(created_courier_credentials)
        new_credentials = helpers.generate_new_courier_credentials()
        login_data['login'] = new_credentials['login']

        login_response = request.login_courier(login_data)

        assert login_response.status_code == 404
        assert "message" in login_response.json()
        assert login_response.json()["message"] == data.MESSAGE_NOT_FOUND

    @allure.title('Невалидные креды (пароль)')
    @allure.description('Тест авторизации при не верном пароле')
    def test_courier_login_with_incorrect_password(self, created_courier_credentials):
        login_data = helpers.create_login(created_courier_credentials)
        new_credentials = helpers.generate_new_courier_credentials()
        login_data['password'] = new_credentials['password']

        login_response = request.login_courier(login_data)

        assert login_response.status_code == 404
        assert "message" in login_response.json()
        assert login_response.json()["message"] == data.MESSAGE_NOT_FOUND

    @allure.title('Пустое поле логина')
    @allure.description('Тест проверяет авторизацию курьера с пустым логином для заполнения')
    def test_courier_login_with_empty_login(self, created_courier_credentials):
        login_data = helpers.create_login(created_courier_credentials)
        login_data['login'] = ''

        login_response = request.login_courier(login_data)

        assert login_response.status_code == 400
        assert "message" in login_response.json()
        assert login_response.json()["message"] == data.ERROR_LOGIN_WITH_EMPTY_FIELD

    @allure.title('Пустое поле пароля')
    @allure.description('Тест проверяет авторизацию курьера с пустым паролем для заполнения')
    def test_courier_login_with_empty_password(self, created_courier_credentials):
        login_data = helpers.create_login(created_courier_credentials)
        login_data['password'] = ''

        login_response = request.login_courier(login_data)

        assert login_response.status_code == 400
        assert "message" in login_response.json()
        assert login_response.json()["message"] == data.ERROR_LOGIN_WITH_EMPTY_FIELD