################################################################################
# Author: Michael Curry
# Date: 03/08/2021
# This program asks users to input potential prime numbers and see if they are
# or aren't.
################################################################################
n = int(input('Enter a positive integer (-1 to quit): '))

def main(): # Main function
    is_prime(n)
    # return same

def is_prime(n): # Prime number filter, sees if value is or not
    if (n < 1):
        return False
 
    while n != -1: # Loop that asks for prime number until you input -1
        if n == 2:
            print(f'{n} is a prime number.') # Prime number check 1
        elif n == 1:
            print(f'{n} is not a prime number.')
        for i in range(2, n):
            if n == 2:
                print(f'{n} is a prime number.') # Prime number check 2
                break
            elif (n % i == 0):
                print(f'{n} is not a prime number.') # Not prime number check 1
                break
            else:
                print(f'{n} is a prime number.') # Prime number check 3
                break
                
        n = int(input('Enter a positive integer (-1 to quit): '))

if __name__ == '__main__':
    main()