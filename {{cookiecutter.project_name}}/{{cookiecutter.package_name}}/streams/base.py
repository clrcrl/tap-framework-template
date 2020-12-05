import singer
import singer.utils
import singer.metrics

from {{ cookiecutter.package_name }}.state import incorporate, save_state

from tap_framework.streams import BaseStream as base
from {{ cookiecutter.package_name }}.cache import stream_cache


LOGGER = singer.get_logger()


class BaseStream(base):
    KEY_PROPERTIES = ["id"]
    CACHE = False
    BASE_URL = "{{ cookiecutter.api_base_url }}"


    def get_params(self):
        # TODO: Update this based on your API
        params = {}
        return params

    def sync_paginated(self, params):
        table = self.TABLE

        while True:
            response = self.client.make_request(
                url, self.API_METHOD, params=params)
            transformed = self.get_stream_data(response)

            with singer.metrics.record_counter(endpoint=table) as counter:
                singer.write_records(table, transformed)
                counter.increment(len(transformed))

            if self.CACHE:
                stream_cache[table].extend(transformed)

            # TODO: Update pagination logic
            meta = response.get("meta", {})
            next_page = meta.get("next", "")

            if next_page:
                params['cursor'] = next_cursor
            else:
                break

    def sync_data(self):
        table = self.TABLE
        LOGGER.info("Syncing data for {}".format(table))
        url = self.BASE_URL + self.PATH
        params = self.get_params()
        self.sync_paginated(url, params)

        return self.state

    def get_stream_data(self, response):
        transformed = []

        for record in response[self.response_key()]:
            record = self.transform_record(record)
            transformed.append(record)

        return transformed
