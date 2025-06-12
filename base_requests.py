import requests

from logger import logger


class BaseReq:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get_request(self, url="", params=None, headers=None):
        response = requests.get(f"{self.base_url}{url}", params=params, headers=headers)
        try:
            logger.info("OK. URL: %s, Code: %d", self.base_url + url, response.status_code)
            logger.debug("json: %s", response.json())
            return response
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None
