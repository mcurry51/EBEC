################################################################################
# Author: Michael Curry
# Date: 04/05/2021
# Description From a user input, convert letters to numbers, so that the client
# can have easier visability.
################################################################################
    
def main():

    number = str(input('Enter a telephone number: ')) # User input
    translated = convert_number(number)
    print(f'The phone number is {translated}') # Print statements

    return

def convert_number(number):

    number_conv = number.upper() # Making them all uppercase
    new_list = [] # Empty list

    for letter in number_conv: # Case statements below
        if (letter == 'A') or (letter == 'B') or (letter == 'C'):
            digit = '2'
            new_list.append(digit)
        elif (letter == 'D') or (letter == 'E') or (letter == 'F'):
            digit = '3'
            new_list.append(digit)
        elif (letter == 'G') or (letter == 'H') or (letter == 'I'):
            digit = '4'
            new_list.append(digit)
        elif (letter == 'J') or (letter == 'K') or (letter == 'L'):
            digit = '5'
            new_list.append(digit)
        elif (letter == 'M') or (letter == 'N') or (letter == 'O'):
            digit = '6'
            new_list.append(digit)
        elif (letter == 'P') or (letter == 'Q') or (letter == 'R') or (letter == 'S'):
            digit = '7'
            new_list.append(digit)
        elif (letter == 'T') or (letter == 'U') or (letter == 'V'):
            digit = '8'
            new_list.append(digit)
        elif (letter == 'W') or (letter == 'X') or (letter == 'Y') or (letter == 'Z'):
            digit = '9'
            new_list.append(digit)
        else:
            new_list.append(letter) # For the 555 and the '-'

    return ''.join(new_list) # Returning the conjoined list

if __name__ == '__main__':
    main()
