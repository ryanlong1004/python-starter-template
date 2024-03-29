""" 
Using environment variables and .env files

`pip install python-dotenv`

https://saurabh-kumar.com/python-dotenv/

"""
import os
from dotenv import dotenv_values


config = dotenv_values(".env")
# config = {"USER": "foo", "EMAIL": "foo@example.org"}

config = {
    **dotenv_values(".env.shared"),  # load shared development variables
    **dotenv_values(".env.secret"),  # load sensitive variables
    **os.environ,  # override loaded values with environment variables
}
