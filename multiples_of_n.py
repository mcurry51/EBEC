################################################################################
# Author: Michael Curry
# Date: 03/29/2021
# Description To write a function that accepts an integer and list, and output
# the list containing elements that are multiples of the integer
################################################################################

def main():
    number_list = [19, 2940, -189, 10, 28, -58, 1, 85, 201, -15, 122, 799, 406] # List
    n = int(input('')) # Integer
    new_list = multiples_of(n,number_list)

    # Print Statements 

    print('Original list of numbers:')
    print(number_list)
    print(f'Numbers in the list that are multiples of {n}:')
    print(new_list)
    print('\n') # New line

    return new_list

    # Multiples function

def multiples_of(n,number_list):
    mult_list = []
    for j in number_list:
        if (j % n == 0):
            mult_list.append(j)
    return mult_list

if __name__ == '__main__':
    main()
