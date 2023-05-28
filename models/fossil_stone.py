"""
Module: fossil_stone.py

This module defines the FossilStone class, which represents
a fossil stone object.

Attributes:
- name (str): The name of the stone.
- color (str): The color of the stone.
- energy_burned_per_gram (int): The amount of energy burned per gram of the fossil stone.
- price_per_gram (int): The price per gram of the stone.
- weight_in_grams (int): The weight of the stone in grams.

Methods:
- __str__(self):
    Returns a string representation of the `FossilStone` object.

- get_full_price(self):
    Calculates and returns the full price of the fossil stone.
"""

from models.stone import Stone


class FossilStone(Stone):
    """
    This class represents an FossilStone.
    It defines common properties and methods.
    """
    def __init__(self, name=0, color=0, energy_burned_per_gram=0,
                 price_per_gram=0, weight_in_grams=0):
        """
        Initializes an FossilStone object with the specified attributes.

        Args:
            name (str): The name of the stone.
            color (str): The color of the stone.
            energy_burned_per_gram (int): The amount of energy burned per gram
            of the fossil stone.
            price_per_gram (int): The price per gram of the stone.
            weight_in_grams (int): The weight of the stone in grams.
        """
        super().__init__(name, color, price_per_gram, weight_in_grams)
        self.energy_burned_per_gram = energy_burned_per_gram

    def __str__(self):
        """
        Returns a string representation of the `FossilStone` object.

        Returns:
            str: A string representation of the `FossilStone` object.
        """
        return f"name: {self.name}, color: {self.color}, " \
               f"energy burned per gram: {self.energy_burned_per_gram}, " \
               f"price per gram: {self.price_per_gram}, weight in grams: {self.weight_in_grams}"

    def get_full_price(self):
        """
        Calculates and returns the full price of the precious stone.

        Returns:
            int: The full price of the precious stone.
        """
        return self.price_per_gram * self.energy_burned_per_gram
