#!/usr/bin/env python3

# Created by: Ahmad
# Created on: Jan 2021
# This program uses an array


import random
array = []


def max(array):
    for loop in range(0, 9):
        number = random.randint(1, 100)
        array.append(number)
    print("Here is a list of random numbers:\n")


    for loop in range(0, 9):
        print("The random number", loop + 1, "is:", array[loop])
    large = array[0]


    for loop in range(1, len(array)):
        if array[loop] > large:
            large = array[loop]
    return large


large = max(array)
print("\nThe largest number is", large)
