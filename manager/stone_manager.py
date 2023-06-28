"""
Module: stone_manager.py

This module defines the StoneManager class, which represents
a stone_manager object.


Methods:
- __str__(self):
    Returns a string representation of the `GemStone` object.

- get_full_price(self):
    Calculates and returns the full price of the gemstone.
"""

from models.gemstone import GemStone
from models.fossil_stone import FossilStone
from models.precious_stone import PreciousStone
from models.artificial_precious_stone import ArtificialPreciousStone


class StoneManager:
    """
    This class represents a StoneManager.
    A class to manage a stones.
    """
    def __init__(self):
        """
        Initializes a StoneManager object with the specified attributes.

        Args:
            stones[] (list): list of stones.
            current_position (int): the index of a current position in list of stones
        """
        self.stones = []
        self.current_position = 0

    def __len__(self):
        """
        Returns the number of stones in the collection.

        Returns:
            int: A number of stones in collection.
        """
        return len(self.stones)

    def __iter__(self):
        """
        Returns the iterator object for iterating over the stones.

        Returns:
            iterator object: the iterator object.
        """
        return self

    def __getitem__(self, item):
        """
        Returns a stone at a given index number.

        Returns:
            stone: object "stone" at a given index.
        """
        return self.stones[item]

    def __next__(self):
        """
        Returns the next stone in the iteration.

        Returns:
            current_stone: the stone that is reached by incrementing.
        """
        if self.current_position < len(self.stones):
            current_stone = self.current_position
            self.current_position += 1
            return current_stone
        else:
            raise StopIteration

    def add_stone(self, stone):
        """
        Adds a stone to the collection
        """
        self.stones.append(stone)

    def find_stones_with_price_per_gram_higher_than(self, price):
        """
        Finds stones with a price per gram higher than the given price.

        Args:
            price (int): The price per gram threshold.

        Returns:
            list: A list of stones matching the criteria.
        """
        return [stone for stone in self.stones if stone.price_per_gram > price]

    def find_stones_by_color(self, color):
        """
        Finds stones with a color that equals to a given one.

        Args:
            color (str): The price per gram threshold.

        Returns:
            list: A list of stones matching the color.
        """
        return [stone for stone in self.stones if stone.color == color]

    def get_full_price_list(self):
        """
        Calculates and returns the full price of the stones.

        Returns:
            list: a list of the full prices of the stones.
        """
        return [stone.get_full_price() for stone in self.stones]


if __name__ == "__main__":
    stone_manager = StoneManager()
    stones = [
        PreciousStone("diamondo", "blue", 50, 99, 3, 15, 100),
        PreciousStone("emeraldo", "green", 50, 99, 3, 20, 100),
        ArtificialPreciousStone("ruby", "red", "lpnu", 10, 100),
        ArtificialPreciousStone("fake diamondo", "aqua", "lnu", 5, 100),
        FossilStone("coal", "black", 50, 20, 100),
        FossilStone("turf", "brown", 50, 20, 100),
        GemStone("amethyst", "purple", 50, 25, 100),
        GemStone("sapphire", "blue", 50, 30, 100)
    ]

    for stone in stones:
        stone_manager.add_stone(stone)

    print("\nStones with price higher than:")
    stones_with_price_per_gram_higher_than = stone_manager.find_stones_with_price_per_gram_higher_than(15)
    for stone in stones_with_price_per_gram_higher_than:
        print(stone)

    print("\nStones with selected colors:")
    stones_with_matching_colors = stone_manager.find_stones_by_color("blue")
    for stone in stones_with_matching_colors:
        print(stone)

    STONES_LIST_LENGTH = len(stones)
    stones_full_price_list = stone_manager.get_full_price_list()
    all_higher_values_than = {num: num > 500 for num in stones_full_price_list if num > 500}

    print(f"\nAmount of stones in list is: {STONES_LIST_LENGTH}")
    print(f"Full stones price list: {stones_full_price_list}")
    print(f"All elements with price higher than: {all_higher_values_than}")

    iterator = iter(stone_manager.stones)
    print("\nAll stones:")
    while True:
        try:
            stone = next(iterator)
            print(stone)
        except StopIteration:
            break

    print("\nEnumerate usage:")
    for index, stone in enumerate(stones):
        print(index, stone)

    print("\nZip usage:")
    for stone, full_price in zip(stones, stones_full_price_list):
        print(f"Stone: {stone}, Full price: {full_price}")
        
    print("\nDictionary usage:")
    dictionary_of_stones_with_chosen_type_params = [{key: value for key, value in stone.dict.items()
                                                     if isinstance(value, str)} for stone in stones]
    print(dictionary_of_stones_with_chosen_type_params)
    
