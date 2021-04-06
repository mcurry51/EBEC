################################################################################
# Author: Michael Curry
# Date: 03/15/2021
# Description: A program that outputs a hex spiral, matching the given 
# parameters and conditions.
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width('5')
    # --------------------------------------------------------------------------

    # Write your code here

    for b in range(39):
        if b == 0 :
            forward(6)
        elif (b*60) % 6 == 0:
            right(60)
            forward(6*b+6)

        else:
            forward((b*6)-6)
    right(60)

# Don't change this
if __name__ == '__main__':
    main()
    done()
