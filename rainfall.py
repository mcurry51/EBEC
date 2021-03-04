################################################################################
# Author: Michael Curry
# Date: 02/28/2021
# This program calculates the total rainfall, average rainfall per month
# given the amount of years.
################################################################################
year = int(input('Enter the number of years: '))
total_rainfall = []
# Nested Loops
if year > 0: # Year Entry
    for y in range(year): # For loop
        print(f'  For year No. {y+1}')
        jan = float(input('    Enter the rainfall for Jan.: '))
        while jan < 0:
            print('    Invalid input, please try again.')
            jan = float(input('    Enter the rainfall for Jan.: '))
        total_rainfall.append(jan)
        feb = float(input('    Enter the rainfall for Feb.: '))
        while feb < 0:
            print('    Invalid input, please try again.')
            feb = float(input('    Enter the rainfall for Feb.: '))
        total_rainfall.append(feb)
        mar = float(input('    Enter the rainfall for Mar.: '))
        while mar < 0:
            print('    Invalid input, please try again.')
            mar = float(input('    Enter the rainfall for Mar.: '))
        total_rainfall.append(mar)
        apr = float(input('    Enter the rainfall for Apr.: '))
        while apr < 0:
            print('    Invalid input, please try again.')
            apr = float(input('    Enter the rainfall for Apr.: '))
        total_rainfall.append(apr)
        may = float(input('    Enter the rainfall for May.: '))          
        while may < 0:
            print('    Invalid input, please try again.')
            may = float(input('    Enter the rainfall for May.: '))
        total_rainfall.append(may)
        jun = float(input('    Enter the rainfall for Jun.: '))
        while jun < 0:
            print('    Invalid input, please try again.')
            jun = float(input('    Enter the rainfall for Jun.: '))
        total_rainfall.append(jun)
        jul = float(input('    Enter the rainfall for Jul.: '))
        while jul < 0:
            print('    Invalid input, please try again.')
            jul = float(input('    Enter the rainfall for Jul.: '))
        total_rainfall.append(jul)
        aug = float(input('    Enter the rainfall for Aug.: '))
        while aug < 0:
            print('    Invalid input, please try again.')
            aug = float(input('    Enter the rainfall for Aug.: '))
        total_rainfall.append(aug)
        sep = float(input('    Enter the rainfall for Sep.: '))
        while sep < 0:
            print('    Invalid input, please try again.')
            sep = float(input('    Enter the rainfall for Sep.: '))
        total_rainfall.append(sep)
        octo = float(input('    Enter the rainfall for Oct.: '))
        while octo < 0:
            print('    Invalid input, please try again.')
            octo = float(input('    Enter the rainfall for Oct.: '))
        total_rainfall.append(octo)
        nov = float(input('    Enter the rainfall for Nov.: '))
        while nov < 0:
            print('    Invalid input, please try again.')
            nov = float(input('    Enter the rainfall for Nov.: '))
        total_rainfall.append(nov)
        dec = float(input('    Enter the rainfall for Dec.: '))
        while dec < 0:
            print('    Invalid input, please try again.')
            dec = float(input('    Enter the rainfall for Dec.: '))
        total_rainfall.append(dec)
    sum_rainfall = sum(total_rainfall) # Sum of rainfall
    num_months = len(total_rainfall) # Number of months
    rainfall_sum = f'{float(sum_rainfall):.2f}' 
    average = float(sum_rainfall) / float(num_months)
    average_float = f'{float(average):.2f}'
# Print Statements
    print(f'There are {num_months} months.')
    print(f'The total rainfall is {rainfall_sum} inches.')
    print(f'The monthly average rainfall is {average_float} inches.')
else: # Invalid Year
    print('Invalid input.')

