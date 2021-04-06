###############################################################################
# Author: Michael Curry 
# Date: 03/21/2021
# Description: Do rock, paper, scissors with a computer.
###############################################################################
from random import *
import random as r

def main():
    # Write your mainline logic here ------------------------------------------
    choice_player = get_player_choice()
    choice_computer = get_computer_choice()
    print(f'  The computer chose {choice_computer}, and you chose {choice_player}.')
    get_winner(choice_computer, choice_player)
    print('Thanks for playing.')
    return

def get_computer_choice():
    r_p_s = ['rock','paper','scissors']
    choice = r.choice(r_p_s)
    return choice

def get_player_choice():
    player_choice = str(input('Choose rock, paper, or scissors: '))
    if (player_choice == 'rock') or (player_choice == 'paper') or (player_choice == 'scissors'):
        return player_choice
    else:
        while not any([player_choice == 'rock',
                       player_choice == 'paper',
                       player_choice == 'scissors']):
            print('You made an invalid choice. Please try again.')
            player_choice = str(input('Choose rock, paper, or scissors: '))
        return player_choice

def get_winner(choice_computer,choice_player):
    if (choice_computer== 'paper') and (choice_player == 'rock'):
        print('  paper beats rock')
        print('  You lost. Better luck next time.')
        return 'computer'
    elif (choice_computer == 'rock') and (choice_player == 'paper'):
        print('  paper beats rock')
        print('  You won the game!')
        return 'player'
    elif (choice_computer == 'scissors') and (choice_player == 'rock'):
        print('  rock beats scissors')
        print('  You won the game!')
        return 'player'
    elif (choice_computer == 'rock') and (choice_player == 'scissors'):
        print('  rock beats scissors')
        print('  You lost. Better luck next time.')
        return 'computer'
    elif (choice_computer == 'paper') and (choice_player == 'scissors'):
        print('  scissors beats paper')
        print('  You won the game!')
        return  'player'
    elif (choice_computer == 'scissors') and (choice_player == 'paper'):
        print('  scissors beats paper')
        print('  You lost. Better luck next time.')
        return 'computer'
    elif choice_computer == choice_player:
        print('  Its a tie. Starting over.')
        print('')
        while choice_player == choice_computer:
            choice_player = get_player_choice()
            choice_computer = get_computer_choice()
        get_winner(choice_computer,choice_player)
        return 'tie'
    return
# Don't change this -----------------------------------------------------------
if __name__ == '__main__':
    main()
