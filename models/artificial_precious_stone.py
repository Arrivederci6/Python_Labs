from models.stone import Stone


class ArtificialPreciousStone(Stone):
    def __init__(self, name=0, color=0, laboratory_name=0, price_per_gram=0, weight_in_grams=0):
        """Calling the parental constructor"""
        super().__init__(name, color, price_per_gram, weight_in_grams)
        """Args:
            name: name of the stone.
            color: color of the stone.
            laboratory_name: laboratory name where stone was created.
            price_per_gram: stone`s price per gram.
            weight_in_grams: stone`s weight in gram."""
        self.laboratory_name = laboratory_name

    def __str__(self):
        """Overriding the __str___ method to get the full string of objects that we have made"""
        return f"name: {self.name}, color: {self.color}, laboratory name: {self.laboratory_name}, " \
               f"weight in grams: {self.weight_in_grams}, price per gram: {self.price_per_gram}, " \
               f"price per gram: {self.price_per_gram}, weight in grams: {self.weight_in_grams}"

    def get_full_price(self):
        """Function from which we are getting the full price by multiplying price per gram by weight in grams"""
        return self.price_per_gram * self.weight_in_grams
