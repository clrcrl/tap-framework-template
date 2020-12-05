import time
import requests
import singer
import zlib
import json
import base64


from tap_framework.client import BaseClient
from requests.auth import HTTPBasicAuth


LOGGER = singer.get_logger()


class {{ cookiecutter.python_class_prefix }}Client(BaseClient):
    def __init__(self, config):
        super().__init__(config)

        self.user_agent = self.config.get("user_agent")
        self.token = self.config.get("token")

    def get_authorization(self):
        pass

    def get_headers(self):
        # TODO: Update this based on your API
        headers = {
            "Content-Type": "application/json",
        }
        if self.user_agent:
            headers["User-Agent"] = self.user_agent
        return headers

    def make_request(self, url, method, base_backoff=45,
                     params=None, body=None):
        # TODO: Update this based on your API
        auth = self.get_authorization()
        headers = self.get_headers()

        LOGGER.info("Making {} request to {}".format(method, url))

        response = requests.request(
            method,
            url,
            headers=headers,
            auth=auth,
            params=params)

        if response.status_code == 429:
            LOGGER.info('Got a 429, sleeping for {} seconds and trying again'
                        .format(base_backoff))
            time.sleep(base_backoff)
            return self.make_request(url, method, base_backoff * 2, params, body)

        if response.status_code != 200:
            raise RuntimeError(response.text)

        return response.json()
