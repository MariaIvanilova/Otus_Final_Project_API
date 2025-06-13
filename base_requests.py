import requests
from logger import logger
import json


class BaseReq:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def get_request(self, url="", params=None, headers=None):
        try:
            response = requests.get(
                f"{self.base_url}{url}", params=params, headers=headers
            )
            logger.info(
                "OK. URL: %s, Request: %s, Code: %d",
                self.base_url + url,
                response.request,
                response.status_code,
            )
            logger.debug("json: %s", response.json())
            return response
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None

    def post_request(self, url="", headers=None, body=None):
        try:
            response = requests.post(
                f"{self.base_url}{url}", headers=headers, data=json.dumps(body)
            )
            logger.info(
                "OK. URL: %s, Request: %s, Code: %d",
                self.base_url + url,
                response.request,
                response.status_code,
            )
            try:
                logger.debug("Response: %s", response.json())
            except ValueError:
                logger.debug("Response (non-JSON): %s", response.text)
            return response
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None

    def delete_request(self, url="", headers=None):
        try:
            response = requests.delete(f"{self.base_url}{url}", headers=headers)
            logger.info(
                "OK. URL: %s, Request: %s, Code: %d",
                self.base_url + url,
                response.request,
                response.status_code,
            )
            try:
                logger.debug("Response: %s", response.json())
            except ValueError:
                logger.debug("Response (non-JSON): %s", response.text)
            return response
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None
