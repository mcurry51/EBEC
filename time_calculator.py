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
if days:
    print(f'  {inp} seconds is: ', end='')
    print(f'{days} day(s)', end ='')
    if hours:
        print(' and ', end ='')
        print(f'{hours} hours(s)', end ='')
    if minutes:
        print(' and ', end ='')
        print(f'{minutes} minutes(s)', end ='')
    if seconds:
        print(' and ', end ='')
        print(f'{seconds} seconds(s)', end ='')
elif hours:
    print(f'  {inp} seconds is: ', end='')
    print(f'{hours} hours(s)', end ='')
    if minutes:
        print(' and ', end ='')
        print(f'{minutes} minute(s)', end ='')
    if seconds:
        print(' and ', end='')
        print(f'{seconds} second(s)', end ='')
elif minutes:
    print(f'  {inp} seconds is: ', end='')
    if seconds:
        print(' and ', end ='')
    print(f'{minutes} minute(s)', end ='')
else:
    print('  The number of seconds is less than one minute', end='')
print('.')