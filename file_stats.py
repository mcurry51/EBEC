################################################################################
# Author: Michael Curry
# Date: 04/05/2021
# Description Accepts a text file, outputs the total number of lines, the total
# number of words and the average words per lines.
################################################################################
def main():

    f = open('rumpelstiltskin.txt', 'r')
    total_num_lines = [lines.split() for lines in f.readlines()] # Reading the file
    f.close() # Close file
    words = []
    length = len(total_num_lines) # Number of lines

    for lines in total_num_lines:
        for word in lines:
            words.append(word)

    num_words = len(words) # Number of words
    average = num_words / length # Average
    average_form = f'{float(average):.1f}' # Average formatted

    # Print statements

    print(f'Total number of words: {num_words}')
    print(f'Total number of lines: {length}')
    print(f'Average number of words per line: {average_form}')

    return

if __name__ == '__main__':
    main()
