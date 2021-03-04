################################################################################
# Author: Michael Curry
# Date: 02/28/2021
# This program sums up the value given by the individual,
# then sums and takes the average of all the inputted values.
################################################################################
starting_num = float(input('Enter a non-negative number (negative to quit): '))
sum_list = [] # Empty list to append to
if starting_num < 0: # Checks to see if inputted number is a positive number
    print('No input.')
else:
    while starting_num >= 0: # Starts the 'input value' process
        sum_list.append(starting_num)
        starting_num = float(input('Enter a non-negative number (negative to quit): '))
    sum_total = sum(sum_list) # Taking sum of list
    sum_total_float = f'{float(sum(sum_list)):.2f}'
    average =  sum_total / len(sum_list) # Averaging the list
    average_float = f'{float(sum_total / len(sum_list)):.2f}'
    print(f'Sum = {sum_total_float}')
    print(f'Average = {average_float}')
