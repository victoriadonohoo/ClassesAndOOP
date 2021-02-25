def main():

    import CarClass as c
    myCar = c.Car("1990 Honda", "Civic")
    
    print( "Accelerating 5 times")

    for i in range(5):
        myCar.accelerate()
        print (myCar.get_speed(myCar))

    print ("Decelerating 5 times")

    for i in range(5):  
        myCar.brake()
        print (myCar.get_speed(myCar))

main()
