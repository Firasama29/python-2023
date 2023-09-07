#tuples are like lists, except they are immutable and are encased in parenthises instead of square brackets
t = (1,2,3,1,4,1,1,5)
print(f"this is a tuple: {t}")

#operations
##built-in functions
###indexing
print(f"element of index 2 is {t.index(2)}")

###counting
print(f"number of times {t[0]} appears is {t.count(1)}")

##getting the type
print(f"t is a {type(t)}")

##length
print(f"t contains {len(t)} elements")

##slicing


##adding a new element will throw an error because tuples are immutable
#t[8]= 7 will throw:
   #TypeError: 'tuple' object does not support item assignment

