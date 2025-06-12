import pytest
from reqres_api import ReqresApi

reqres_api = ReqresApi("https://reqres.in", "reqres-free-v1")


def test_get_users_list_status():
    response = reqres_api.get_single_users(1)
    assert response.status_code == 200


def test_get_single_user_not_found():
    response = reqres_api.get_list_users(1)
    data = response.json()
    total_pages = data["total_pages"]
    per_page = data["per_page"]
    user_not_found_id = (total_pages * per_page) + 1
    response = reqres_api.get_single_users(user_not_found_id)
    assert response.status_code == 404


@pytest.mark.parametrize("user_id", [0, -1, "ivan"])
def test_get_single_user_negative(user_id):
    response = reqres_api.get_single_users(user_id)
    assert response.status_code == 404
