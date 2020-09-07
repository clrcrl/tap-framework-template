#!/usr/bin/env python3

import singer

import tap_framework

from {{ cookiecutter.package_name }}.client import {{ cookiecutter.python_class_prefix }}Client
from {{ cookiecutter.package_name }}.streams import AVAILABLE_STREAMS

LOGGER = singer.get_logger()  # noqa


class {{ cookiecutter.python_class_prefix }}Runner(tap_framework.Runner):
    pass


@singer.utils.handle_top_exception(LOGGER)
def main():
    args = singer.utils.parse_args(required_config_keys=["token"])
    client = {{ cookiecutter.python_class_prefix }}Client(args.config)
    runner = {{ cookiecutter.python_class_prefix }}Runner(args, client, AVAILABLE_STREAMS)

    if args.discover:
        runner.do_discover()
    else:
        runner.do_sync()


if __name__ == "__main__":
    main()
