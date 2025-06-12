import allure
from base_requests import BaseReq


class ReqresApi(BaseReq):
    @allure.step("Запрос GET /api/users?page={page_num}")
    def get_list_users(self, page_num):
        params = {"page": page_num}
        headers = {"X-API-KEY": self.api_key}
        url = "/api/users"
        return self.get_request(url=url, params=params, headers=headers)

    @allure.step("Запрос GET /api/users/{user_id}")
    def get_single_users(self, user_id):
        headers = {"X-API-KEY": self.api_key}
        params = {}
        url = f"/api/users/{user_id}"
        return self.get_request(url=url, params=params, headers=headers)
