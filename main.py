import sign
import rock
import paper
import scissors
import lizard
import spock

import random

play_again = 'Y'

while play_again.upper() == 'Y':
    player = 'None'
    computer = 'None'
    explain = 'N'
    while_loop = True

    # Rules Explained
    while while_loop == True:
        explain = input('Would you like an explanation of the rules? Y/N: ')
        if explain.upper() == 'Y':
            print('')
            print('Rules')
            print('The rules of the game are simple. Similar to rock paper scissors, you just have to choose a symbol to throw out.')
            print('Each symbol is weak to two and strong against two. If you throw out a symbol that is strong against your opponents, you win.')
            print('If you throw out a symbol that is weak against your opponents, you lose. If you throw out the same symbol, you draw. \n')
            print('Symbols:')
            print('Rock (Defeats Scissors and Lizard --- Defeated by Paper and Spock)')
            print('Paper (Defeats Rock and Spock --- Defeated by Scissors and Lizard)')
            print('Scissors (Defeats Paper and Lizard --- Defeated by Rock and Spock)')
            print('Lizard (Defeats Paper and Spock --- Defeated by Rock and Scissors)')
            print('Spock (Defeats Rock and Scissors --- Defeated by Paper and Lizard)')
            while_loop = False
        elif explain.upper() == 'N':
            print('The game will now begin. Good luck!')
            while_loop = False
        else:
            print('Unexpected response. Please try again.')
            continue

    # Computer Chooses Symbol
    computer = random.randint(1,5)
    if computer == 1:
        computer = rock.Rock(['Scissors', 'Lizard'], ['Paper', 'Spock'], ['Rock'])
    elif computer == 2:
        computer = paper.Paper(['Rock', 'Spock'], ['Scissors', 'Lizard'], ['Paper'])
    elif computer == 3:
        computer = scissors.Scissors(['Paper', 'Lizard'], ['Rock', 'Spock'], ['Scissors'])
    elif computer == 4:
        computer = lizard.Lizard(['Spock', 'Paper'], ['Rock', 'Scissors'], ['Lizard'])
    elif computer == 5:
        computer = spock.Spock(['Scissors', 'Rock'], ['Paper', 'Lizard'], ['Spock'])

    # Player Chooses Symbol
    

    # Show Symbols and Declare Winner
    print('')
    print(f'Computer Chose: {computer.draws[0]} \nPlayer Chose: {player.draws[0]}')
    print(f'And the result is...{player.determine_winner(computer)}')
    print('')
    # "Play Again" or "Quit": Perform Appropriate Action
    while_loop = True

    while while_loop == True:

        x = input('Would you like to play again? Y/N: ')

        if x.upper() == 'Y':
            print('Restarting...Good Luck!')
            while_loop = False
        elif x.upper() == 'N':
            print('Thanks for playing!')
            while_loop = False
            play_again = 'N'
        else:
            print('Unexpected response. Please try again. \n')