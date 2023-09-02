# use for, split() and if to create a statement that will print the words that start with an 's'
str = 'Print only the words that start with S in this sentence'

for i in str.split():
    if i[0] == 's' or i[0] == 'S':
        print(i)


# use range() to print all the even numbers from 0 to 20
print('\nusing for loop:')
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
print("alternate solution using List comprehension:")
print([i for i in range(1, 21) if i % 2 == 0])

# use List Comprehension to print a list of all numbers between 1 and 50 that are divisible by 3
print('\nbelow numbers are divisible by 3')
print([num for num in range(1, 51) if num % 3 == 0])


# print the word 'even' for any word with even number of letters in below setence
str = 'Print every word in this sentence that has an even number of letters'
#----> for loop
print('\nwords that have even number of letters:')
#----> using for loop
for even in str.split():
    if len(even) % 2 == 0:
        print(even)

#----> using List comprehension
print('\nsame result using list comprehension:')
print([even for even in str.split() if len(even) % 2 == 0])

# write a program that prints integers from 1 to 50, but for multiples of 3, print 'Fizz'
# and multiples of 5, print 'Buzz' and for multiples of both 3 and 5 print 'FizzBuzz'
print('\nFizzBuzz for numbers divisible by 3 or 5 or both')
for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# write a program that prints a list of the first letters of every word in below sentence:
sentence = 'Create a list that prints the first letters of every word in this sentence'
print("\nhere's the first letters of every word in the above string:")
for letter in sentence.split():
    print(letter[0])

print([letter[0] for letter in sentence.split()])