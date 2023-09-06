#dictionaries are a key-value data structures in python

firas = {
	"name": "Firas",
	"age": 31,
	"profession": "developer"
}

print(firas)

#adding one element
firas['passion'] = 'programming'


#adding a list as an element
firas['languages'] = ['java', 'python', 'javascript']

#let's see the output
print("I'm %s, I'm %d years old and I'm a %s. My passion is in learning %s languages such as %s, %s and %s" % (firas['name'], firas['age'], firas['profession'], firas['passion'], firas['languages'][0], firas['languages'][1], firas['languages'][2]))


#let's iterate through the dictionary
for key in firas:
	print("%s: %s" % (key, firas[key]))


#another way using items() function
print("\nMy details printed using items() function")
for attribute, item in firas.items():
	print("%s: %s" % (attribute, item))
