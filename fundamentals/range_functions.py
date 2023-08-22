#range() function is used to generate sequence of numbers and is used in loops for iteration
#the following are common ways to use range() function

#function(stop): generates a sequence of numbers until 'stop' - 1
for i in range(5):
    print(i)

#function(start, stop): generates a sequence from 'start' until 'stop' - 1
for x in range(1, 7):
    print(x)

#function(start, stop, step): generates a sequence from 'start' until 'stop' - 1, incrementing by 'step'
for y in range(0, 10, 2):
    print(y)