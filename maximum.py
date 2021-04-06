################################################################################
# Author: Michael Curry
# Date: 03/21/2021
# This program asks utilize two seperate functions, one function to compare two
# numbers and distance per second, and another one to run the progam all together.
################################################################################
def main(): # Main function
    first_int = int(input('Enter the first integer: ')) # Integer input 1
    second_int = int(input('Enter the second integer: ')) # Integer input 2

    max_of_two(first_int, second_int)

def max_of_two(first_int, second_int): # Function that compares two integers
    if first_int < second_int:
        print(f'{second_int} is greater.')
        return second_int
    if first_int > second_int:
        print(f'{first_int} is greater.')
        return first_int
    if first_int == second_int:
        return 0

if __name__ == '__main__':
    main()