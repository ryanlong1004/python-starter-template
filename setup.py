#!/usr/bin/env python
# -*- coding: utf-8 -*-

# pylint: disable=missing-module-docstring

import os
import sys
import subprocess

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

if sys.argv[-1] == "publish":
    subprocess.call(f"{sys.executable} setup.py sdist bdist_wheel upload", shell=False)
    sys.exit()

required = ["click"]

setup(
    name="new_project",
    version="0.0.0",
    description="new_project description",
    # long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Ryan Long",
    author_email="ryan.long@noaa.gov",
    url="",
    py_modules=["new_project"],
    install_requires=required,
    tests_require=["pytest"],
    license="MIT",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    extras_require={  # Optional
        "dev": [
            "check-manifest",
            "black",
            "pylint",
            "pytest",
            "pytest-cov",
            "pytest-xdist",
            "tox",
            "icecream"
        ],
        "test": ["pytest", "pytest-cov", "pytest-forked", "pytest-xdist", "tox"],
    },
    packages=find_packages()
)
