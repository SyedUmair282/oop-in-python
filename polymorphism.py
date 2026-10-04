class Car:
    def start(self):
        print("Engine start...!!")

class Bike:
    def start(self):
        print("Motor start...!!")

class Ship:
    def start(self):
        print("Ship start...!!")

car = Car()
bike = Bike()
ship = Ship()

for x in [car, bike, ship]:
    x.start()