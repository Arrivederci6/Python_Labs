from abc import ABC, abstractmethod


class Stone(ABC):
    def __init__(self, name, color, price_per_gram, weight_in_grams):
        self.name = name
        self.color = color
        self.weight_in_grams = weight_in_grams
        self.price_per_gram = price_per_gram

    def __str__(self):
        return f"name:{self.name}, color: {self.color}"

    @abstractmethod
    def get_full_price(self):
        pass
