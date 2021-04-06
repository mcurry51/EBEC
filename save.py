################################################################################
# Author: Michael Curry
# Date: 03/08/2021
# This program asks users to input scores, and output the graded of each score
# as well as the average of all scores.
################################################################################
def main():
    counter = 0
    while counter < 5:
        scort = get_valid_score()
        determine_grade(scort)
        counter += 1
    scores = get_valid_score()
    calc_average(scores)
    return

def get_valid_score():
    count = 0
    grades = []

    while count < 5:
        score = float(input('Enter a score: '))
        if score < 0 or score > 100:
            while score < 0 or score > 100:
                print('Invalid Input. Please try again.')
                grade_score = float(input('Enter a score: '))
                score = grade_score
            if score > 0 and score <= 100:
                grades.append(score)
                
        else:
            grades.append(score)
            
        count += 1
    return score

def determine_grade(score):
    if score >= 90 and score <= 100:
        print(f'The letter grade for {score} is A.')
        return 'A'
    elif score >= 80 and score < 90:
        print(f'The letter grade for {score} is B.')
        return 'B'
    elif score >= 70 and score < 80:
        print(f'The letter grade for {score} is C.')
        return 'C'
    elif score >= 60 and score < 70:
        print(f'The letter grade for {score} is D.')
        return 'D'
    else:
        print(f'The letter grade for {score} is F.')
        return 'F'

def calc_average(grades):
    average = sum(grades) / len(grades)
    average_formatted = f'{average:.1f}'
    average_formatted_again = float(average_formatted)
    print(type(average_formatted_again))
    print(f'The average score is {average_formatted_again}.')
    return average_formatted

if __name__ == '__main__':
    main()