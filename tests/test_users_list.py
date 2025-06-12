import pytest
import allure
from reqres_api import ReqresApi

reqres_api = ReqresApi("https://reqres.in", "reqres-free-v1")


@allure.title("Проверка статус-кода (200 OK)")
def test_get_users_list_status():
    response = reqres_api.get_list_users(1)
    assert response.status_code == 200


@allure.title(
    "Проверка структуры ответа на запрос: /api/users?page=1"
    "JSON с полями page, per_page, total, total_pages, data"
)
def test_get_users_list_structure():
    response = reqres_api.get_list_users(1)
    data = response.json()

    assert "page" in data
    assert "per_page" in data
    assert "total" in data
    assert "total_pages" in data
    assert "data" in data and isinstance(data["data"], list)


@allure.title("Проверка пагинации.Ключ 'page' содержит корректное значение")
@pytest.mark.parametrize("page_num", [1, 2, 10])
def test_pagination_works(page_num):
    response = reqres_api.get_list_users(page_num)
    data = response.json()
    assert data["page"] == page_num


@allure.title("Проверка пустой страницы. Возврат пустой data")
def test_empty_page_returns_empty_data():
    response = reqres_api.get_list_users(1)
    data = response.json()
    total_pages = data["total_pages"]
    response = reqres_api.get_list_users(
        total_pages + 1
    )  # total_pages + 1 - the page doesn't exist
    data = response.json()
    assert data["data"] == []


@allure.title(
    "Проверка структуры данных пользователя:"
    " data должен содержать обязательные поля (id, email, first_name, last_name, avatar"
)
def test_user_data_structure():
    response = reqres_api.get_list_users(2)
    users = response.json()["data"]

    required_fields = {"id", "email", "first_name", "last_name", "avatar"}
    for user in users:
        assert all(field in user for field in required_fields)


@allure.title(
    "Негативный тест. Параметр page содержит невалидное значение. Выводится page=1"
)
@pytest.mark.parametrize("page_num", [0, -1, "test"])
def test_get_users_list_negative(page_num):
    response = reqres_api.get_list_users(page_num)
    users_first_id = response.json()["data"][0]["id"]
    assert response.status_code == 200
    assert users_first_id == 1
