################################################################################
# Author: Michael Curry
# Date: 03/08/2021
# This program asks users to input scores, and output the graded of each score
# as well as the average of all scores.
################################################################################
def main():
    counter = 1
    grades =[]
    while counter <= 5: # Loop for obtaining 5 input  grades
        scort = get_valid_score()
        grades.append(scort)
        determine_grade(scort)
        counter += 1
    calc_average(grades)
    return

def get_valid_score(): # Function for inputting the individual scores
    score = float(input('Enter a score: '))
    if score < 0 or score > 100:
        while score < 0 or score > 100: # While loop if the score is unacceptable
            print('Invalid Input. Please try again.')
            grade_score = int(input('Enter a score: '))
            score = grade_score
        return score
    else:
        return score

def determine_grade(score):# Function for determine the grade of said individual score
    if score >= 90 and score <= 100:
        print(f'The letter grade for {float(score)} is A.')
        return 'A'
    elif score >= 80 and score < 90:
        print(f'The letter grade for {float(score)} is B.')
        return 'B'
    elif score >= 70 and score < 80:
        print(f'The letter grade for {float(score)} is C.')
        return 'C'
    elif score >= 60 and score < 70:
        print(f'The letter grade for {float(score)} is D.')
        return 'D'
    else:
        print(f'The letter grade for {float(score)} is F.')
        return 'F'

def calc_average(grades): # Function for calculating the average
    average = sum(grades) / len(grades)
    average_formatted = f'{average:.2f}'
    print(f'The average score is {average_formatted}.')
    return average

if __name__ == '__main__':
    main()