import random

class Insect:

    def __init__(self, w, l, f):
        self.__legs = l
        self.__wings = w
        self.__flight = f

    def flight_length(self):
        self.__flight = random.randint(1, 10)
        return self.__flight

    def get_legs(self):
        return self.__legs
    def get_wings(self):
        return self.__wings
    

    #def __str__(self):
#        return print("wings: ", str(self.__wings), "\n", "legs: ", str(self.__legs),

