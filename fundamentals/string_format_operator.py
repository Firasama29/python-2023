#the % operator is used for string formatting. It allows you to insert a value into a placeholder
#within the main string.
#the format specifier %s is used to insert string values
#the format specifier %d is used to insert integer values
#the format specifier %f is used to insert float values
###NOTE: the % operator is used for simple string formatting. For more complex and modern
#formatting, f-strings are used
name = 'Firas'
age = 31
myString = "My name is %s and I'm %d years old" % (name, age)

print(myString)

#f-strings