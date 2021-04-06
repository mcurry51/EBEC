################################################################################
# Author: 
# Date: 
# Description ...
################################################################################

# Don't change this
from turtle import *

def main():

    # Don't change this block --------------------------------------------------
    setup(564, 564)
    width(7)
    side_length = 60 # Also the radius of a circle enclosed by the star.
    penup()
    goto(0, -side_length) # Start at the bottom of the star.
    pendown()
    # --------------------------------------------------------------------------

    # Write your code here
    begin_fill()
    right(18)
    forward(50)
    left(18)
    left(90)
    forward(50)
    right(36)
    forward(50)
    left(108)
    forward(50)
    right(36)
    forward(50)
    left(108)
    forward(50)
    end_fill()
# Sorry I couldn't finish this
# Don't change this
if __name__ == '__main__':
    main()
    done()
