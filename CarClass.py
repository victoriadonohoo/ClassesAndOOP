class Car:
    
    def __init__(self, model, make):
        self.__yearmodel = model
        self.__make = make
        self.__speed = 0
    
    def accelerate(self):
        self.__speed += 5 

    def brake(self):
        self.__speed -= 5
    
    def get_speed(self, speed):
        return self.__speed
    

