from models.gemstone import GemStone
from models.fossil_stone import FossilStone
from models.precious_stone import PreciousStone
from models.artificial_precious_stone import ArtificialPreciousStone


class StoneManager:
    def __init__(self):
        self.stones = []

    def add_stone(self, stone):
        self.stones.append(stone)

    def find_stones_with_price_per_gram_higher_than(self, price):
        return list(filter(lambda stone: stone.price_per_gram > price, self.stones))

    def find_stones_by_color(self, color):
        return list(filter(lambda stone: stone.color == color, self.stones))


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

    for _ in stones:
        stone_manager.add_stone(_)
        print(_)

    print("\nStones with price higher than:")
    stones_with_price_per_gram_higher_than = stone_manager.find_stones_with_price_per_gram_higher_than(15)
    for _ in stones_with_price_per_gram_higher_than:
        print(str(_))

    print("\nStones with selected colors:")
    stones_with_matching_colors = stone_manager.find_stones_by_color("blue")
    for _ in stones_with_matching_colors:
        print(str(_))
