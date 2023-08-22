#dictionaries are a key-value data structures in python
firas = {
    "name": "firas",
    "age": 31,
    "profession": "developer"
}

def print_details():
    
    print(firas)

    #adding a new element
    firas['current focus'] = 'learning python'

    #adding a list as a element
    firas['languages'] = ['java', 'python', 'javascript']


    #let's print the output
    return "I'm %s, %d years old and I'm a %s. I'm currently focusing on %s. I love %s, %s and %s." % (firas['name'], firas['age'], firas['profession'], firas['current focus'], firas['languages'][0], firas['languages'][1], firas['languages'][2])


#let's call the function
print_details()
