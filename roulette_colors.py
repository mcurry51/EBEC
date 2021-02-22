################################################################################
# Author: Michael Curry
# Date: 02/22/2021
# This program enters a pocket number and displays 
# whether the pocket is green, red, or black.
################################################################################
pocket = int(input('Please enter a pocket number: ')) # Enter Pocket
if pocket == 0: print('  Pocket 0 is green.') # Conditional Check 1
elif pocket in range(1,11): print(f'  Pocket {pocket} is black.') if pocket % 2 == 0 else print(f'  Pocket {pocket} is red.') # Conditional Check 2
elif pocket in range(11,19): print(f'  Pocket {pocket} is red.') if pocket % 2 == 0 else print(f'  Pocket {pocket} is black.') # Conditional Check 3
elif pocket in range(19,29): print(f'  Pocket {pocket} is black.') if pocket % 2 == 0 else print(f'  Pocket {pocket} is red.') # Conditional Check 4
elif pocket in range(29,37): print(f'  Pocket {pocket} is red.') if pocket % 2 == 0 else print(f'  Pocket {pocket} is black.') # Conditional Check 6
else: print("  Invalid Input!") # Conditional Check 7

