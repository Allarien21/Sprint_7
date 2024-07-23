import requests
import allure
import urls


@allure.step('Запрос на создание курьера')
def create_courier(data):
    return requests.post(urls.CREATE_COURIER, json=data)


@allure.step('Запрос на удаление курьера')
def delete_courier(courier_id):
    return requests.delete(urls.DELETE_COURIER + str(courier_id))


@allure.step('Запрос логина курьера')
def login_courier(data):
    return requests.post(urls.LOGIN_COURIER, json=data)


@allure.step('Запрос на создание заказа')
def create_order(order):
    return requests.post(urls.CREATE_ORDER, json=order.order_part())


@allure.step('Запрос на получение списка заказов')
def get_orders():
    return requests.get(urls.GET_ORDERS)