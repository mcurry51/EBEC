################################################################################
# Author: Michael Curry
# Date: 02/21/2021
# This program sees if a year 
# is a leap year.
################################################################################
# Input Year
year = int(input('Please input a year: ')) # Year variable
# Calculations
if year % 4 == 0 and year % 100 == 0 and year % 400 == 0: # First Conditonal Check
     print(f'In the year {year}, there are 29 days in February.')
elif year % 4 == 0 and year % 100 != 0: # Second Conditonal Check
     print(f'In the year {year}, there are 29 days in February.')
elif (year % 4 and year % 100) == 0 and year % 400 != 0: # Third Conditonal Check
     print(f'In the year {year}, there are 28 days in February.')
elif year % 4 == 0 and (year % 100 and year % 400 != 0): # Fourth Conditonal Check
     print(f'In the year {year}, there are 28 days in February.')
elif year % 4 != 0: # Fifth Conditonal Check
     print(f'In the year {year}, there are 28 days in February.')
elif year % 400 != 0: # Sixth Conditonal Check
     print(f'In the year {year}, there are 28 days in February.')
else: # Final
     print(f'In the year {year}, there are 28 days in February.')