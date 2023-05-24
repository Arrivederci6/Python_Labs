from models.stone import Stone


class PreciousStone(Stone):
    """ A class that represents precious stone"""
    instance = None

    def __init__(self, name=0, color=0, carat=0, clarity=0, price_per_carat=0, price_per_gram=0, weight_in_grams=0):
        """Calling the parental constructor"""
        super().__init__(name, color, price_per_gram, weight_in_grams)
        """Args:
            name: name of the stone.
            color: color of the stone.
            carat: stone`s carat amount.
            clarity: stone`s clarity amount
            price_per_gram: stone`s price per gram.
            weight_in_grams: stone`s weight in gram."""
        self.carat = carat
        self.clarity = clarity
        self.price_per_carat = price_per_carat

    @staticmethod
    def get_instance(self):
        if PreciousStone.instance is None:
            PreciousStone.instance = PreciousStone()

        return PreciousStone.instance

    def __str__(self):
        """Overriding the __str___ method to get the full string of objects that we have made"""
        return f"name: {self.name}, color: {self.color}, carat: {self.carat}, " \
               f"clarity: {self.clarity}, price per carat: {self.price_per_carat}, " \
               f"price per gram: {self.price_per_gram}, weight in grams: {self.weight_in_grams}"

    def get_full_price(self):
        """Function from which we are getting the full price by multiplying carat by price per carat"""
        return self.carat * self.price_per_carat

    def increase_clarity_by_one(self):
        """The function in which we are increasing our existing clarity by 1 (one)"""
        self.clarity += 1
        return self.clarity

    def increase_price_by_percentage(self, percentage):
        """The function in which we are getting an increased price by n-th amount of percents"""
        return self.clarity * (percentage / 100)
