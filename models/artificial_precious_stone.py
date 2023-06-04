"""
Module: artificial_precious_stone.py

This module defines the ArtificialPreciousStone class, which represents
an artificial precious stone object.

Attributes:
- name (str): The name of the stone.
- color (str): The color of the stone.
- laboratory_name (str): The laboratory name in which the stone was created.
- price_per_gram (int): The price per gram of the stone.
- weight_in_grams (int): The weight of the stone in grams.

Methods:
- __str__(self):
    Returns a string representation of the `ArtificialPreciousStone` object.

- get_full_price(self):
    Calculates and returns the full price of the artificial precious stone.
"""

from models.stone import Stone
from exceptions.invalid_weight_exception import InvalidWeightException


class ArtificialPreciousStone(Stone):
    """
    This class represents an ArtificialPreciousStone.
    It defines common properties and methods.
    """
    def __init__(self, name=0, color=0, laboratory_name=0, price_per_gram=0, weight_in_grams=0):
        """
        Initializes an ArtificialPreciousStone object with the specified attributes.

        Args:
            name (str): The name of the stone.
            color (str): The color of the stone.
            laboratory_name (str): The laboratory name where the stone was created.
            price_per_gram (int): The price per gram of the stone.
            weight_in_grams (int): The weight of the stone in grams.
        """
        super().__init__(name, color, price_per_gram, weight_in_grams)
        self.laboratory_name = laboratory_name

    def __str__(self):
        """
        Returns a string representation of the `ArtificialPreciousStone` object.

        Returns:
            str: A string representation of the `ArtificialPreciousStone` object.
        """
        return f"name: {self.name}, color: {self.color}, laboratory name: {self.laboratory_name}, "\
               f"weight in grams: {self.weight_in_grams}, price per gram: {self.price_per_gram}, "\
               f"price per gram: {self.price_per_gram}, weight in grams: {self.weight_in_grams}"

    def get_full_price(self):
        """
        Calculates and returns the full price of the precious stone.
        If the weight is <= 0 - raises an exception

        Returns:
            int: The full price of the precious stone.
            OR
            InvalidWeightException(raise): If the weight is <= 0 .
        """
        if self.weight_in_grams <= 0:
            exception_message = "Weight must be greater than 0!"
            raise InvalidWeightException(exception_message)
        return self.price_per_gram * self.weight_in_grams
