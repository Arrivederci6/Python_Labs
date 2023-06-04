"""
Module: stone.py

This module defines an abstract class Stone.

Attributes:
- name (str): The name of the stone.
- color (str): The color of the stone.
- price_per_gram (int): The price per gram of the stone.
- weight_in_grams (int): The weight of the stone in grams.

Methods:
- str(self):
    Returns a string representation of the stone.

- get_full_price(self):
    Abstract method to calculate the full price of the stone.
"""
from abc import ABC, abstractmethod


class Stone(ABC):
    """
    This abstract class represents a stone object. It defines common properties and behaviors
    for stone subclasses.
    """
    def __init__(self, name, color, price_per_gram, weight_in_grams):
        """
        Initializes a stone object with the specified attributes.

        Args:
            name (str): The name of the stone.
            color (str): The color of the stone.
            price_per_gram (int): The price per gram of the stone.
            weight_in_grams (int): The weight of the stone in grams.
        """
        self.name = name
        self.color = color
        self.weight_in_grams = weight_in_grams
        self.price_per_gram = price_per_gram

    def __str__(self):
        """
        Returns a string representation of the stone.

        Returns:
            str: A string representation of the stone.
        """
        return f"name:{self.name}, color: {self.color}"

    @abstractmethod
    def get_full_price(self):
        """
        Abstract method to calculate the full price of the stone.
        Subclasses must implement this method.

        Returns:
            int: The full price of the stone.
        """
