"""
Module: precious_stone.py

This module defines the PreciousStone class, which represents a precious stone object.

Attributes:
- instance (PreciousStone): The singleton instance of the PreciousStone class.
- name (str): The name of the stone.
- color (str): The color of the stone.
- carat (int): The carat amount of the stone.
- clarity (int): The clarity index of the stone.
- price_per_carat (int): The price per carat of the stone
- price_per_gram (int): The price per gram of the stone.
- weight_in_grams (int): The weight of the stone in grams.

Methods:
- get_instance():
    Returns the singleton instance of the `PreciousStone` class.

- __str__(self):
    Returns a string representation of the `PreciousStone` object.

- get_full_price(self):
    Calculates and returns the full price of the precious stone.

- increase_clarity_by_one(self):
    Increases the clarity of the precious stone by one.

- increase_price_by_percentage(self, percentage):
    Calculates and returns the increased price of the precious stone by a given percentage.
"""

from models.stone import Stone


class PreciousStone(Stone):
    """
    This class represents a PreciousStone.
    It defines common properties and methods.
     """
    instance = None

    def __init__(self, name=0, color=0, carat=0, clarity=0, price_per_carat=0,
                 price_per_gram=0, weight_in_grams=0):
        """
        Initializes a `PreciousStone` object with the specified attributes.

        Args:
            name (str): The name of the stone.
            color (str): The color of the stone.
            carat (int): The carat amount of the stone.
            clarity (int): The clarity amount of the stone.
            price_per_carat (int): The price per carat of the stone.
            price_per_gram (int): The price per gram of the stone.
            weight_in_grams (int): The weight of the stone in grams.
        """
        super().__init__(name, color, price_per_gram, weight_in_grams)
        self.carat = carat
        self.clarity = clarity
        self.price_per_carat = price_per_carat

    @staticmethod
    def get_instance():
        """
        Returns the singleton instance of the `PreciousStone` class.

        Returns:
            PreciousStone: The singleton instance of the `PreciousStone` class.
        """
        if PreciousStone.instance is None:
            PreciousStone.instance = PreciousStone()

        return PreciousStone.instance

    def __str__(self):
        """
        Returns a string representation of the `PreciousStone` object.

        Returns:
            str: A string representation of the `PreciousStone` object.
        """
        return f"name: {self.name}, color: {self.color}, carat: {self.carat}, " \
               f"clarity: {self.clarity}, price per carat: {self.price_per_carat}, " \
               f"price per gram: {self.price_per_gram}, weight in grams: {self.weight_in_grams}"

    def get_full_price(self):
        """
        Calculates and returns the full price of the precious stone.

        Returns:
            int: The full price of the precious stone.
        """
        return self.carat * self.price_per_carat

    def increase_clarity_by_one(self):
        """
        Increases the clarity of the precious stone by one.

        Returns:
            int: The new clarity value.
        """
        self.clarity += 1
        return self.clarity

    def increase_price_by_percentage(self, percentage):
        """
        Calculates and returns the increased price of the precious stone by a given percentage.

        Args:
            percentage (float): The percentage value to increase the price.

        Returns:
            float: The increased price of the precious stone.
        """
        return self.clarity * (percentage / 100)
