class PreciousStone:
    def __init__ (self, name, carat, color, clarity, price_per_carat):
        self.name = name
        self.carat = carat
        self.color = color
        self.clarity = clarity
        self.price_per_carat = price_per_carat

    def get_total_price(self):
        return self.carat * self.price_per_carat

    def increase_clarity_by_one(self):
        self.clarity += 1
        return self.clarity

    def increase_price_by_percentage(self, percentage):
        increased_price = self.clarity * (percentage / 100)
        return increased_price

new_stone = PreciousStone('Emeraldo', 10, 'Green', 50, 5)

total_price = new_stone.get_total_price()
print("The total price is:", total_price)

increased_clarity = new_stone.increase_clarity_by_one()
print("The increased clarity is:", increased_clarity)

increased_price = new_stone.increase_price_by_percentage(10)
print("The increased price is:", increased_price)