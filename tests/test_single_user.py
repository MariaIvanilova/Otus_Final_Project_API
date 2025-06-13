import allure
import pytest
from reqres_api import ReqresApi

reqres_api = ReqresApi("https://reqres.in", "reqres-free-v1")


@allure.title("GET. Проверка статус-кода (200 OK)")
def test_get_users_list_status():
    response = reqres_api.get_single_users(1)
    assert response.status_code == 200


@allure.title("GET. ID пользователя не найден. Status_code = 404")
def test_get_single_user_not_found():
    response = reqres_api.get_list_users(1)
    data = response.json()
    total_pages = data["total_pages"]
    per_page = data["per_page"]
    user_not_found_id = (total_pages * per_page) + 1
    response = reqres_api.get_single_users(user_not_found_id)
    assert response.status_code == 404


@allure.title("GET. ID пользователя некорректен. Status_code = 404")
@pytest.mark.parametrize("user_id", [0, -1, "ivan"])
def test_get_single_user_negative(user_id):
    response = reqres_api.get_single_users(user_id)
    assert response.status_code == 404


@allure.title(
    "GET. Проверка структуры данных пользователя:"
    " data должен содержать обязательные поля (id, email, first_name, last_name, avatar"
)
def test_single_user_data_structure():
    response = reqres_api.get_single_users(1)
    user = response.json()["data"]

    required_fields = {"id", "email", "first_name", "last_name", "avatar"}
    assert all(field in user for field in required_fields)


@allure.title("POST. Проверка статус-кода (201 Created)")
def test_post_user():
    body = {"name": "morpheus", "job": "leader"}
    response = reqres_api.post_user(body)
    assert response.status_code == 201


@allure.title("POST. Структура ответа")
def test_post_user_data_structure():
    body = {"name": "morpheus", "job": "leader"}
    response = reqres_api.post_user(body)
    user = response.json()
    required_fields = {"name", "job", "id", "createdAt"}
    assert all(field in user for field in required_fields)


@allure.title("POST. Проверка создания пользователя с разными данными")
@pytest.mark.parametrize(
    "name, job",
    [("Neo", "Developer"), ("A" * 100, "B" * 100), ("", ""), ("123", "!@#$%^")],
)
def test_post_user_with_various_data(name, job):
    response = reqres_api.post_user(body={"name": name, "job": job})
    assert response.status_code == 201
    user = response.json()
    assert user["name"] == name
    assert user["job"] == job


@allure.title("POST. Проверка при невалидных/неполных данных")
@pytest.mark.parametrize(
    "body, expected_code",
    [
        (None, 400),
        ({"name": "Alice"}, 201),
        ({"job": "Developer"}, 201),
        ("invalid json", 400),
        ('{"name": "Alice",}', 400),
    ],
)
def test_post_user_invalid_data(body, expected_code):
    response = reqres_api.post_user(body=body)
    assert response.status_code == expected_code


@allure.title("DELETE. Проверка статус-кода (204 No content)")
def test_delete_user():
    response = reqres_api.delete_user(1)
    assert response.status_code == 204


@allure.title("DELETE. Проверка тела ответа")
def test_delete_user_response_body():
    response = reqres_api.delete_user(1)
    assert response.text == ""


@allure.title("DELETE. Параметризованный тест для разных ID. API возвращает 204")
@pytest.mark.parametrize(
    "user_id, expected_code",
    [
        (999999, 204),  # Несуществующий ID
        (0, 204),  # Некорректный ID
        ("abc", 204),  # Нечисловой ID
    ],
)
def test_delete_user_parameterized(user_id, expected_code):
    response = reqres_api.delete_user(user_id)
    assert response.status_code == expected_code
