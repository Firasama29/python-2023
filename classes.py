#pyton classes, 
#objects,
#init() function,
#how to create an object of a class,
#how to call instance variables and functions of a class

class Vehicle:
	name = ""
	color = ""
	price = 0

	def describe(self):
		return "%s is a %s car worth more than MYR %.2f ." % (self.name, self.color, self.price)


myCar = Vehicle()
myCar.name = "Honda civic"
myCar.color = "brown"
myCar.price = 30000

print(myCar.describe())
