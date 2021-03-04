################################################################################
# Author: Michael Curry
# Date: 02/28/2021
# This program inserts hashes, per the inputted amount 
# of lines given by the user.
################################################################################
num_hash = int(input('Enter the number of lines: ')) # User enters an amount of lines

for num in range(num_hash): # For loop, relating to the number of lines
    print('#', end='')
    if num == 0:
        print('#')
    else:
        for n in range(num): # For loop, relating to the amount of spaces needing to be entered
            print(' ', end='')
        print('#')