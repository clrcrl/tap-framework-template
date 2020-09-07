#!/usr/bin/env python

from setuptools import setup, find_packages
import os.path

setup(
    name="{{ cookiecutter.project_name }}",
    version="0.0.1",
    description="Singer.io tap for extracting data from the {{ cookiecutter.data_source }} API",
    author="Fishtown Analytics",
    url="http://fishtownanalytics.com",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["{{ cookiecutter.package_name }}"],
    install_requires=["tap-framework==0.0.4",],
    entry_points="""
          [console_scripts]
          {{ cookiecutter.project_name }}={{ cookiecutter.package_name }}:main
      """,
    packages=find_packages(),
    package_data={"{{ cookiecutter.package_name }}": ["schemas/*.json"]},
)
