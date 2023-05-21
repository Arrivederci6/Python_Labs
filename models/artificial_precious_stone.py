from models.stone import Stone


class ArtificialPreciousStone(Stone):
    def __init__(self, name=0, color=0, laboratory_name=0, price_per_gram=0, weight_in_grams=0):
        super().__init__(name, color, price_per_gram, weight_in_grams)
        self.laboratory_name = laboratory_name

    def __str__(self):
        return f"name: {self.name}, color: {self.color}, laboratory name: {self.laboratory_name}, " \
               f"weight in grams: {self.weight_in_grams}, price per gram: {self.price_per_gram}, " \
               f"price per gram: {self.price_per_gram}, weight in grams: {self.weight_in_grams}"

    def get_full_price(self):
        return self.price_per_gram * self.weight_in_grams
