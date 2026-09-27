class Car:
    model = 'Tesla'
    year = 2026
    color = 'black'

# for one object
auto = Car()
print(auto.model, auto.year, auto.color)

# for multiple objects of same class
auto2 = Car()
auto3 = Car()
auto4 = Car()
print(auto2.model, auto3.year, auto4.color)

# del object
del auto4
# print(auto4.model) gives an error bcz its delete

class Fruit:
    def __init__(self, name, season):
        self.name = name
        self.season = season
    
    def greetFruit(self):
        print("Welcome " + self.name + " for your season " + self.season)
    # to print what ever you want as a class
    def __str__(self):
        return "Welcome " + self.name + " for your season " + self.season

fruit1 = Fruit("Mango", "Summer")
fruit1.greetFruit()

fruit1.expiry = 2022
print(fruit1.expiry)

print(fruit1)
