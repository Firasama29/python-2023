#classes
#objects
#init() function
#how to create an object of a class
#how to call instance variables and functions of a class
#what is self

class Vehicle:
    name = ""
    color = ""
    price = ""

    def describe(self):
        return "%s is a %s car worth more than MYR %.2f." % (self.name, self.color, self.price)

#creating an instance of Vehicle class
myCar = Vehicle()
myCar.name = "honda civic"
myCar.color = "grey"
myCar.price = 45000

print(myCar.describe())

