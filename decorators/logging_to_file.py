"""
Module: logging_to_file.py

This module represents a logger decorator that logs exceptions into text file.

Attributes:
    - None

Methods:
    - None

Functions:
    - logging_to_file (outer function)
"""

import logging
import sys
from exceptions.invalid_weight_exception import InvalidWeightException


def logging_to_file(func):
    """
    Decorator that logs files into text file

    Args:
        - func(function): the function to decorate

    Returns:
        - decorated function
    """
    logging.basicConfig(filename='error.log', level=logging.ERROR,
                        format='%(asctime)s - %(levelname)s - %(message)s\n%(pathname)s:%(lineno)d')

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except InvalidWeightException as e:
            logging.error(str(e))
            sys.exit()

    return wrapper
