year = int(input('Please input a year: ')) # Year variable
four = 4  # Variable for dividend 4
hundred = 100  # Variable for dividend 100
fhundred = 400  # Variable for dividend 400

checkune = year % 4  # First condition
checkdeux = year % 100  # Second condition
checktrois = year % 400  # Third condition

if checkune == 0 and checkdeux == 0 and checktrois == 0:
     print(f'In the year {year}, there are 29 days in February.')
elif checkune == 0 and checkdeux != 0:
     print(f'In the year {year}, there are 29 days in February.')
elif (checkune and checkdeux) == 0 and checktrois != 0:
     print(f'In the year {year}, there are 28 days in February.')
elif checkune == 0 and (checkdeux and checktrois != 0):
     print(f'In the year {year}, there are 28 days in February.')
elif checkune != 0:
     print(f'In the year {year}, there are 28 days in February.')
elif checktrois != 0:
     print(f'In the year {year}, there are 28 days in February.')
else:
     print(f'In the year {year}, there are 28 days in February.')