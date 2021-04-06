###############################################################################
# Author: Michael Curry
# Date: 3/22/2021
# Description:   The function shouldhave one argument which specifies how many 
# digits the random number it returns shouldhave. Then use this function in a 
# program that gives the user a simple math quiz.
###############################################################################
from random import *
import random as r

def main():
    for _ in range(2,4):
        if _ == 2:
            x = random_number(_)
        else:
            y = random_number(_)
    #Formatting
    format_x = f'{(x):5,.0f}'
    format_y = f'{(y):4,.0f}'

    #Printing Statements
    print(format_x)
    print('+', end='')
    print(format_y)
    print('-----')

    #Summation
    sum_x_y = x + y

    #User guess
    user_guess = int(input('= '))

    #Guess checker
    if user_guess == sum_x_y:
        print('Correct -- Good Work!')
    else:
        print(f'Incorrect. The correct answer is {sum_x_y}.')
    return

def random_number(arg):
    #Random integers
    range_start = 10**(arg-1)
    range_end = (10**arg)-1
    return randint(range_start, range_end)


# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
