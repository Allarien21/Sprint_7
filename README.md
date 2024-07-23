Sprint_7
=====================
API Tests
--------------------


### Описание файлов:

1. conftest -  файл с фикстурами на создание кредов
2. helpers - основные действия работы с запросами
3. request - методы запросов 
4. data - файл с данными
5. urls - список ручек


___

###  Файл test_create_courier.py

1. ***test_create_courier*** - Проверка на успешное создание курьера
2. ***test_create_duplicated_courier*** - Проверка на создание дубликата курьера
3. ***test_create_courier_with_empty_fields*** - Параметризованный тест,проверка с пустыми обязательными полями
4. ***test_create_courier_with_missing_field*** - Проверка с пропущенным полем
___


###  Файл test_create_order.py

1. ***test_create_order*** - Параметризованный тест, создание успешного заказа
___


###  Файл test_login_courier.py

1. ***test_courier_login_successful*** - Проверка на успешную авторизацию курьера
2. ***test_courier_login_with_incorrect_login*** - Проверка на невальдные данные(логин)
3. ***test_courier_login_with_incorrect_password*** - Проверка на невальдные данные(пароль)
4. ***test_courier_login_with_empty_login*** - Проверка авторизации с пустым полем логина
5. ***test_courier_login_with_empty_password*** - Проверка авторизации с пустым полем пароля
___

###  Файл test_login_courier.py

1. ***test_get_all_orders*** - Проверка на успешное получение списка всех заказов
___