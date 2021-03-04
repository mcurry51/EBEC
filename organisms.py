################################################################################
# Author: Michael Curry
# Date: 02/28/2021
# This program inserts hashes, per the inputted amount 
# of lines given by the user.
################################################################################
initial_pop = int(input('Starting number, in million: ')) # Input statement for Pop.
daily_increase = int(input('Average daily increase, in percent: ')) # Input statement for Pop. rate
days_to_multiply = int(input('Number of days to multiply: ')) # Input statement for days for multiplying.
print('Day   Approx. Pop')
for r in range(days_to_multiply): 
    if r == 0:
        initial_pop = initial_pop
        popoulation_formatted = f'{float(initial_pop):8,.4f}'
        day_formatted = f'{float(r+1):3,.0f}'
    else:
        initial_pop *= (1 + daily_increase / 100)
        day_formatted = f'{float(r + 1):3,.0f}'
        popoulation_formatted = f'{float(initial_pop):8,.4f}'
    print(f'{day_formatted}      {popoulation_formatted}')
