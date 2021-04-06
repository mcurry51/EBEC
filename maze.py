################################################################################
# Author: Michael Curry
# Date: 03/15/2021
# Description: A program designed to get the turtle from the center to the right 
# exit.
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    bgpic('maze.png')
    shape('turtle')
    color('green')
    width('5')
    step = 12
    # --------------------------------------------------------------------------

    # Write your code here
    goto(0,12)
    left(180)
    forward(156)
    right(90)
    forward(24)
    left(90)
    forward(48)
    left(90)
    forward(47)
    right(90)
    forward(24)
    right(90)
    forward(240)
    right(90)
    forward(456)
    right(90)
    forward(228)
    left(90)
    forward(24)

# Don't change this
if __name__ == '__main__':
    main()
    done()
