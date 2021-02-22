import CarClass as c

my_car = c.Car('2012 Civic', 'Honda')
start_speed = 0 
speed = c.get_speed

print('Accelerating')

for i in range(5):
    my_car.accelerate()
    my_car.get_speed(start_speed)
    print(my_car.get_speed)
    
print('Braking')

for i in range(5):
    my_car.brake()
    my_car.get_speed(start_speed)
    print(my_car.get_speed)




    

