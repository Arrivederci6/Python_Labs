from models.stone import Stone


class FossilStone(Stone):
    def __init__(self, name=0, color=0, energy_burned_per_gram=0, price_per_gram=0, weight_in_grams=0):
        """Calling the parental constructor"""
        super().__init__(name, color, price_per_gram, weight_in_grams)
        """Creating  objects"""
        self.energy_burned_per_gram = energy_burned_per_gram

    def __str__(self):
        """Overriding the __str___ method to get the full string of objects that we have made"""
        return f"name: {self.name}, color: {self.color}, energy burned per gram: {self.energy_burned_per_gram}, " \
               f"price per gram: {self.price_per_gram}, weight in grams: {self.weight_in_grams}"

    def get_full_price(self):
        """Function from which we are getting the full price by multiplying price per gram by energy burned per gram"""
        return self.price_per_gram * self.energy_burned_per_gram
