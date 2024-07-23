from dataclasses import dataclass
import random
import string
import request
import allure
from faker import Faker
fake = Faker()
@allure.step("Генерация данных для регистрации")
def generate_new_courier_credentials(empty_field=None):
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    credentials = {
        "login": login,
        "password": password,
        "firstName": first_name
    }
    if empty_field is not None:
        credentials[empty_field] = ""
    return credentials

@allure.step("Создание кредов")
def create_login(credentials):
    return {
        'login': credentials['login'],
        'password': credentials['password']
    }

@allure.step("Авторизация курьера")
def login_courier(credentials):
    login_data = create_login(credentials)
    login_response = request.login_courier(login_data)
    courier_id = login_response.json().get('id')
    return courier_id

@allure.step("Регистрация курьера")
def create_courier(register=False):
    credentials = generate_new_courier_credentials()

    if register:
        request.create_courier(credentials)

    return credentials

@allure.step("Удаление курьера")
def delete_courier(credentials):
    courier_id = login_courier(credentials)
    request.delete_courier(courier_id)


@allure.step("создание заказа")
@dataclass
class Order:
    firstName: str
    lastName: str
    address: str
    metroStation: int
    phone: str
    rentTime: int
    deliveryDate: str
    comment: str
    color: [str]

    def order_part(self):
        return {
            "firstName": self.firstName,
            "lastName": self.lastName,
            "address": self.address,
            "metroStation": self.metroStation,
            "phone": self.phone,
            "rentTime": self.rentTime,
            "deliveryDate": self.deliveryDate,
            "comment": self.comment,
            "color": self.color
        }
