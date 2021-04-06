################################################################################
# Author: Michael Curry
# Date: 04/04/2021
# Description To do an in-depth data analysis of the random_numbers.txt file
# created from the previous exercise.
################################################################################
    
def main():
    f = open('random_numbers.txt', 'r')
    new_list = []
    
    with f:
        for lines in f.readlines():
            new_list.append(lines)
    f.close() # Can't forget to close the file! <3

    integers = [int(_) for _ in new_list] # Obtaining a list of the values inside
    sum_form = f'{float(sum(integers)):,.0f}' # Formatted Summation
    avg_form = f'{float(sum(integers)/len(integers)):.1f}' # Formatted average
    length = f'{float(len(integers)):,.0f}' # Formatted length
    print(f'{length} numbers were read from the file.\nMax: {max(integers)}\nMin: {min(integers)}\nSum: {sum_form}\nAvg: {avg_form}') # Full print statament
    
if __name__ == '__main__':
    main()
