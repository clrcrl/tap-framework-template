"""
If you need to adjust the API calls based on the docs, this is the file to do it in
"""
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
