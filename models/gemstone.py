"""
Module: gemstone.py

This module defines the GemStone class, which represents
a gemstone object.

Attributes:
- name (str): The name of the stone.
- color (str): The color of the stone.
- refinement_index (int): The refinement index of the gemstone.
- price_per_gram (int): The price per gram of the stone.
- weight_in_grams (int): The weight of the stone in grams.

Methods:
- __str__(self):
    Returns a string representation of the `GemStone` object.

- get_full_price(self):
    Calculates and returns the full price of the gemstone.
"""

from models.stone import Stone


class GemStone(Stone):
    """
    This class represents an GemStone.
    It defines common properties and methods.
    """
    def __init__(self, name=0, color=0, refinement_index=0, price_per_gram=0, weight_in_grams=0):
        """
        Initializes a GemStone object with the specified attributes.

        Args:
            name (str): The name of the stone.
            color (str): The color of the stone.
            refinement_index (int): The refinement index of the gemstone.
            price_per_gram (int): The price per gram of the stone.
            weight_in_grams (int): The weight of the stone in grams.
        """
        super().__init__(name, color, price_per_gram, weight_in_grams)
        self.refinement_index = refinement_index

    def __str__(self):
        """
        Returns a string representation of the `GemStone` object.

        Returns:
            str: A string representation of the `GemStone` object.
        """
        return f"name: {self.name}, color: {self.color}, refinement index: {self.refinement_index}, " \
               f"price per gram: {self.price_per_gram}, weight in grams: {self.weight_in_grams}"

    def get_full_price(self):
        """
        Calculates and returns the full price of the gemstone.

        Returns:
            int: The full price of the gemstone.
        """
        return self.refinement_index * self.price_per_gram
