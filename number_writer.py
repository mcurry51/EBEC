################################################################################
# Author: Michael Curry
# Date: 04/05/2021
# Description To generate however many random numbers, given by the user, and 
# then 'attaching' those random numbers to a text file.
################################################################################
from random import *
import random as r 

def main():
    number_choice = int(input('Enter the number of random numbers to be written to the file: ')) # User input
    li_list = [] # Empty list to append to 
    lister_0 = [] # Empty list to append to 

    for i in range(number_choice):
        integer = r.randint(1,500) # Random integer between 1 and 500, both included
        li_list.append(integer) # Attaching random integer to list

    for j in li_list:
        brack = j # Getting element in list and converting to string, to attach new line to it
        str_brack = str(brack)
        lister_0.append(str_brack + '\n')

    with open('random_numbers.txt', 'w') as fo: # Opening text file to write to
       fo.writelines(lister_0)
    fo.close() # Can't forget to close! <3
    return

if __name__ == '__main__':
    main()
