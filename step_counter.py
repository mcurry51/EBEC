################################################################################
# Author: Michael Curry
# Date: 04/05/2021
# Description This program utilizes steps from a text file and finds the average
# steps per month.
################################################################################
    
def main():
    f = open('steps.txt', 'r')
    new_list = []
    
    with f:
        for lines in f.readlines():
            new_list.append(lines)
    f.close() # Can't forget to close the file! <3

    integers = [int(_) for _ in new_list] # Obtaining a list of the values inside
    jan = [] # Empty lists to append to
    feb = [] # Empty lists to append to
    mar = [] # Empty lists to append to
    apr = [] # Empty lists to append to
    may = [] # Empty lists to append to
    june = [] # Empty lists to append to
    jul = [] # Empty lists to append to
    aug = [] # Empty lists to append to
    spt = [] # Empty lists to append to
    octo = [] # Empty lists to append to
    nov = [] # Empty lists to append to
    dec = [] # Empty lists to append to

    for _ in range(len(integers)):
        if 0 <= _ and 30 >= _: # There's probably an easier way to do this....oh well
            s = integers[_]
            jan.append(s)
        elif 30 <= _ and 58 >= _: # There's probably an easier way to do this....oh well
            s = integers[_]
            feb.append(s)
        elif 58 <= _ and 89 >= _: # There's probably an easier way to do this....oh well
            s = integers[_]
            mar.append(s)
        elif 89 <= _ and 119 >= _: # There's probably an easier way to do this....oh well
            s = integers[_]
            apr.append(s)
        elif 119 <= _ and 150 >= _: # There's probably an easier way to do this....oh well
            s = integers[_]
            may.append(s)
        elif 150 <= _ and 180 >= _: # There's probably an easier way to do this....oh well
            s = integers[_]
            june.append(s)
        elif 180 <= _ and 211 >= _: # There's probably an easier way to do this....oh well
            s = integers[_]
            jul.append(s)
        elif 211 <= _ and 242 >= _: # There's probably an easier way to do this....oh well
            s = integers[_]
            aug.append(s)
        elif 242 <= _ and 272 >= _: # There's probably an easier way to do this....oh well
            s = integers[_]
            spt.append(s)
        elif 272 <= _ and 303 >= _: # There's probably an easier way to do this....oh well
            s = integers[_]
            octo.append(s)
        elif 303 <= _ and 333 >= _: # There's probably an easier way to do this....oh well
            s = integers[_]
            nov.append(s)
        elif 333 <= _ and 364 >= _: # There's probably an easier way to do this....oh well
            s = integers[_]
            dec.append(s)
        else:
            print('Invalid')
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    sum_Jan_form = f'{float(sum(jan)/len(jan)):2.1f}' # Formatted average for each  month
    sum_Feb_form = f'{float(sum(feb)/len(feb)):2.1f}' # Formatted average for each  month
    sum_Mar_form = f'{float(sum(mar)/len(mar)):2.1f}' # Formatted average for each  month
    sum_Apr_form = f'{float(sum(apr)/len(apr)):2.1f}' # Formatted average for each  month
    sum_May_form = f'{float(sum(may)/len(may)):2.1f}' # Formatted average for each  month
    sum_June_form = f'{float(sum(june)/len(june)):2.1f}' # Formatted average for each  month
    sum_July_form = f'{float(sum(jul)/len(jul)):2.1f}' # Formatted average for each  month
    sum_Aug_form = f'{float(sum(aug)/len(aug)):2.1f}' # Formatted average for each  month
    sum_Sept_form = f'{float(sum(spt)/len(spt)):2.1f}' # Formatted average for each  month
    sum_Oct_form = f'{float(sum(octo)/len(octo)):2.1f}' # Formatted average for each  month
    sum_Nov_form = f'{float(sum(nov)/len(nov)):2.1f}' # Formatted average for each  month
    sum_Dec_form = f'{float(sum(dec)/len(dec)):2.1f}' # Formatted average for each  month

    print('The average steps taken each month were:')
    print(f'{months[0].rjust(10)} : {sum_Jan_form}', ) # Print statements for each month, where I'm sure there is an easier way to code this
    print(f'{months[1].rjust(10)} : {sum_Feb_form}', ) # Print statements for each month, where I'm sure there is an easier way to code this
    print(f'{months[2].rjust(10)} : {sum_Mar_form}', ) # Print statements for each month, where I'm sure there is an easier way to code this
    print(f'{months[3].rjust(10)} : {sum_Apr_form}', ) # Print statements for each month, where I'm sure there is an easier way to code this
    print(f'{months[4].rjust(10)} : {sum_May_form}', ) # Print statements for each month, where I'm sure there is an easier way to code this
    print(f'{months[5].rjust(10)} : {sum_June_form}', ) # Print statements for each month, where I'm sure there is an easier way to code this
    print(f'{months[6].rjust(10)} : {sum_July_form}', ) # Print statements for each month, where I'm sure there is an easier way to code this
    print(f'{months[7].rjust(10)} : {sum_Aug_form}', ) # Print statements for each month, where I'm sure there is an easier way to code this
    print(f'{months[8].rjust(10)} : {sum_Sept_form}', ) # Print statements for each month, where I'm sure there is an easier way to code this
    print(f'{months[9].rjust(10)} : {sum_Oct_form}', ) # Print statements for each month, where I'm sure there is an easier way to code this
    print(f'{months[10].rjust(10)} : {sum_Nov_form}', ) # Print statements for each month, where I'm sure there is an easier way to code this
    print(f'{months[11].rjust(10)} : {sum_Dec_form}', ) # Print statements for each month, where I'm sure there is an easier way to code this

if __name__ == '__main__':
    main()
