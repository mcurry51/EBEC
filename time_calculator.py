################################################################################
# Author: Michael Curry
# Date: 02/21/2021
# This program converts seconds
# to readable time.
################################################################################
inp = int(input('Please enter a time in seconds. ')) # Seconds variable
days = inp // 86400 # Days Calculation
hours = inp % (24 * 3600) // 3600 # Hours Calculation
minutes = inp % 3600 // 60 # Minutes Calculation
seconds = ((inp % (24 * 3600)) % 3600) % 60 # Days Calculation
if inp < 60: print('  The number of seconds is less than one minute.') # Conditional Check 1
elif inp in range(60,3601): print(f' {minutes} minute(s).') if inp % 60 == 0 else print(f' {minutes} minute(s) and {seconds} second(s)') # Conditional Check 2
elif inp in range(3601, 86400): print(f' {hours} hours(s).') if inp % 3600 == 0 else print(f'  {hours} hours(s) and {seconds} second(s)') # Conditional Check 3
elif inp % 86400 == 0: print(f'  {days} day(s).') # Conditional Check 4
else: print(f'  {days} days(s) and {hours} hour(s) and {minutes} minute(s) and {seconds} second(s)') # Conditional Check 5

