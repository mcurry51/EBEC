################################################################################
# Author: Michael Curry
# Date: 03/08/2021
# This program asks utilize two seperate functions, one function to calculate
# the distance per second, and another one to run the progam all together.
################################################################################
def main(): # Main function
    time = 10
    print('Time (s)  Distance (m)\n----------------------')
    for i in range(time):
        print(f'{float(i+1):8,.0f}', end='') # Formatting
        print(f'{float(falling_distance(i+1)):14,.2f}') # Formatting

def falling_distance(time): # Function that calculates the distance per time
    g = 9.81
    distance = 0.5 * g * (time) ** 2
    return distance # Returning distance

if __name__ == '__main__':
    main()