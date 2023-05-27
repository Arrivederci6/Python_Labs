from models.stone import Stone


class GemStone(Stone):
    def __init__(self, name=0, color=0, refinement_index=0, price_per_gram=0, weight_in_grams=0):
        """Calling the parental constructor"""
        super().__init__(name, color, price_per_gram, weight_in_grams)
        """Creating  objects"""
        self.refinement_index = refinement_index

    def __str__(self):
        """Overriding the __str___ method to get the full string of objects that we have made"""
        return f"name: {self.name}, color: {self.color}, refinement index: {self.refinement_index}, " \
               f"price per gram: {self.price_per_gram}, weight in grams: {self.weight_in_grams}"

    def get_full_price(self):
        """Function from which we are getting the full price by multiplying refinement index by price per gram"""
        return self.refinement_index * self.price_per_gram
