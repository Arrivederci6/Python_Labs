class PreciousStone:
    """ A class that represents precious stone"""

    def __init__(self, name, carat, color, clarity, price_per_carat):
        """Initializing objects"""
        self.__name = name
        self.__carat = carat
        self.__color = color
        self.__clarity = clarity
        self.__price_per_carat = price_per_carat
    
    @property
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def carat(self):
        return self.__carat
    
    @carat.setter
    def carat(self, value):
        self.__carat = value
        
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def clarity(self):
        return self.__clarity

    @clarity.setter
    def clarity(self, value):
        self.__clarity = value
       
    @property
    def price_per_carat(self):
        return self.__price_per_carat

    @price_per_carat.setter
    def price_per_carat(self, value):
        self.__price_per_carat = value

    def __str__(self):
        """Overriding the __str___ method to get the full string of objects that we have made"""
        print(f"Name: {self.__name}, Clarity: {self.__clarity}, Color: {self.__color}, Clarity: {self.__clarity}, Price per carat: {self.__price_per_carat}\n")
    
    def get_total_price(self):
        """Function from wich we are getting the full price by multiplying carat by price per carat"""
        return self.__carat * self.__price_per_carat
    
    def increase_clarity_by_one(self):
        """The function in wich we are increasing our existing clarity by 1 (one)"""
        self.__clarity += 1
        return self.__clarity
    
    def increase_price_by_percentage(self, percentage):
        """The function in wich we are getting an increased price by n-th amount of percents"""
        return self.__clarity * (percentage / 100)
    

new_stone = PreciousStone('Emeraldo', 10, 'Green', 50, 5)
new_stone.__str__()
print(new_stone.get_total_price(), new_stone.increase_clarity_by_one(), new_stone.increase_price_by_percentage(10))