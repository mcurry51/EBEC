################################################################################
# Author: Michael Curry
# Date: 02/21/2021
# This program converts seconds
# to readable time for humans, and makes it easier to understand
################################################################################
inp = int(input('Please enter a time in seconds. ')) # Seconds variable
days = inp // 86400 # Days Calculation
hours = inp % (24 * 3600) // 3600 # Hours Calculation
minutes = inp % 3600 // 60 # Minutes Calculation
seconds = ((inp % (24 * 3600)) % 3600) % 60 # Days Calculation
inp_formatted = f'{float(inp):,.0f}' # Formatted input
if days: # If days is true, look at other relationship
    print(f'  {inp_formatted} seconds is: ', end='')
    print(f'{days} day(s)', end ='')
    if hours: # Checks relationship between days and hours
        if minutes:
            if seconds:
                print(f', {hours} hour(s), {minutes} minute(s) and {seconds} second(s).', end ='')
            else:
                print(f', {hours} hour(s) and {minutes} minute(s).', end ='')
        elif seconds: # Checks relationship between days and seconds
            print(f', {hours} hour(s) and {seconds} second(s).', end ='')
        else:
            print(' and ', end='')
            print(f'{hours} hour(s).', end ='')  
    elif minutes: # Checks relationship between days and minutes
            if seconds:
                print(f', {minutes} minute(s) and {seconds} second(s).', end ='')
            else:
                print(f' and {minutes} minute(s).', end ='')
    elif seconds: # Checks relationship between days and seconds
        print(f' and {seconds} second(s).', end ='')
    else:
        print('.')
elif hours: # If hours is true, look at other relationship
    print(f'  {inp_formatted} seconds is: ', end='')
    print(f'{hours} hour(s)', end ='')
    if minutes: # Checks relationship between hours and minutes
        if seconds:
                print(f', {minutes} minute(s) and {seconds} second(s).', end ='')
        else:
            print(f' and {minutes} minute(s).', end ='')
    elif seconds: # Checks relationship between hours and seconds
        print(f' and {seconds} second(s).', end ='')
    else:
        print('.')  
elif minutes: # If minute is true, look at other relationship
    print(f'  {inp_formatted} seconds is: ', end='') # Checks relationship between minutes and seconds
    if seconds:
        print(f'{minutes} minute(s) and {seconds} second(s).', end ='')
    else:
        print(f'{minutes} minute(s).', end ='')
else:
    print('  The number of seconds is less than one minute.', end='')
