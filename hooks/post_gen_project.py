import pathlib

endpoints = {{cookiecutter.endpoints_csv.split(",")}}


cwd = pathlib.Path().absolute()

for endpoint in endpoints:

    # write a file to schemas/
    f = open("{{cookiecutter.package_name}}/schemas/{}.json".format(endpoint), "x")

    # write a file to streams/
    f = open("{{cookiecutter.package_name}}/streams/{}.py".format(endpoint), "x")
    f.write(
        """
from {{cookiecutter.package_name}}.streams.base import BaseStream
import singer

LOGGER = singer.get_logger()


class {0}Stream(BaseStream):
    API_METHOD = "GET"
    TABLE = "{1}"
    KEY_PROPERTIES = ["id"]

    def response_key(self):
        return "data"

    @property
    def path(self):
        return "/{1}"
    """.format(
            "".join(x.capitalize() or "_" for x in endpoint.split("_")), endpoint
        )
    )
