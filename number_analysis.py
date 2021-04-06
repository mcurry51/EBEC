################################################################################
# Author: Michael Curry
# Date: 03/29/2021
# Description To do an analysis of a list created with values given by the user
# thus creating a list, and then analyzing that list
################################################################################

def main():
    # Print Statements Pt. 1
    list_m = get_number_list() # List
    minimu = min(list_m) # Minimum value
    maximu = max(list_m) # Maximum value
    su_m = sum(list_m) # Sum value
    average = su_m / len(list_m) # Average value

    min_for = f'{float(minimu):2,.2f}' # Formatted min
    max_for = f'{float(maximu):2,.2f}' # Formatted max
    sum_for = f'{float(su_m):2,.2f}' # Formatted sum
    average_for =  f'{float(average):2,.2f}' # Formatted average

    # Print statement Pt. 2
    print(f'Lowest number: {min_for}')
    print(f'Highest number: {max_for}')
    print(f'Total: {sum_for}')
    print(f'Average: {average_for}')


    return

def get_number_list():

    list_f = [] # Empty list to append to

    for i in range(1,11):

        i_var = f'{float(i):2,.0f}' # Formatted element
        number_choice = float(input(f'  Enter number {i_var} of 10: ')) # Print statement
        list_f.append(number_choice) # Appending
    
    return list_f

if __name__ == '__main__':
    main()
