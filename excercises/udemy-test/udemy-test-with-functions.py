# write a function that prints the words that start with an 's'
def print_words_starting_with_s():
    sentence = 'Print only the words that start with S in this sentence'

    for i in sentence.split():
        if i[0] == 's' or i[0] == 'S':
            print(i)


# write a function that prints all the even numbers from 0 to 20
def print_even_numbers():
    print('\nusing for loop:')
    for i in range(1, 21):
        if i % 2 == 0:
            print(i)
    print("alternate solution using List comprehension:")
    print([i for i in range(1, 21) if i % 2 == 0])

# write a function that prints a list of all numbers between 1 and 50 that are divisible by 3
def print_numbers_divisible_by_three():
    print('\nbelow numbers are divisible by 3')
    print([num for num in range(1, 51) if num % 3 == 0])

# write a function that prints the word 'even' for any word with even number of letters in below setence
def print_even_words():
    str = 'Print every word in this sentence that has an even number of letters'
    # ----> for loop
    print('\nwords that have even number of letters:')
    # ----> using for loop
    for even in str.split():
        if len(even) % 2 == 0:
            print(even)

    # ----> using List comprehension
    print('\nsame result using list comprehension:')
    print([even for even in str.split() if len(even) % 2 == 0])

# write a function that prints integers from 1 to 50, but for multiples of 3, print 'Fizz'
# and multiples of 5, print 'Buzz' and for multiples of both 3 and 5 print 'FizzBuzz'
def print_fizz_buzz():
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

# write a function that prints a list of the first letters of every word in below sentence:
def print_first_letters():
    sentence = 'Create a list that prints the first letters of every word in this sentence'
    print("\nhere's the first letters of every word in the above string:")
    for letter in sentence.split():
        print(letter[0])

    print("\nusing list comprehension")
    print([letter[0] for letter in sentence.split()])

print_words_starting_with_s()
print_even_numbers()
print_numbers_divisible_by_three()
print_even_words()
print_fizz_buzz()
print_first_letters()