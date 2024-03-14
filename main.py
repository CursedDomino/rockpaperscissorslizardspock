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
    play_again = 'Y'
    explain = 'N'

    # Rock (Defeats Scissors and Lizard --- Defeated by Paper and Spock)
    # Paper (Defeats Rock and Spock --- Defeated by Scissors and Lizard)
    # Scissors (Defeats Paper and Lizard --- Defeated by Rock and Spock)
    # Lizard (Defeats Paper and Spock --- Defeated by Rock and Scissors)
    # Spock (Defeats Rock and Scissors --- Defeated by Paper and Lizard)

    # Rules Explained
    while True:
        explain = input('Would you like an explanation of the rules? Y/N')
        while True:
            if explain.upper() == 'Y':
                print('The rules of the game are simple. Similar to rock paper scissors, you just have to choose a symbol to throw out.')
                print('Each symbol is weak to two and strong against two. If you throw out a symbol that is strong against your opponents, you win.')
                print('If you throw out a symbol that is weak against your opponents, you lose. If you throw out the same symbol, you draw.')
                while True:
                    explain = input('Would you like to know what each symbol is strong and weak against? Y/N')
                    if explain.upper == 'Y':
                        print('Rock (Defeats Scissors and Lizard --- Defeated by Paper and Spock)')
                        print('Paper (Defeats Rock and Spock --- Defeated by Scissors and Lizard)')
                        print('Scissors (Defeats Paper and Lizard --- Defeated by Rock and Spock)')
                        print('Lizard (Defeats Paper and Spock --- Defeated by Rock and Scissors)')
                        print('Spock (Defeats Rock and Scissors --- Defeated by Paper and Lizard)')
                    elif explain.upper == 'N':
                        print('The game will now begin. Good luck!')
                        break
                    else:
                        print('Unexpected response. Please try again.')
                        continue
                break
            elif explain.upper() == 'N':
                print('The game will now begin. Good luck!')
                break
            else:
                print('Unexpected response. Please try again.')
                continue

    # Computer Chooses Symbol
    computer = random.randint(1,5)
    if computer == 1:
        pass
    elif computer == 2:
        pass
    elif computer == 3:
        pass
    elif computer == 4:
        pass
    elif computer == 5:
        pass

    # Player Chooses Symbol
    # Show Symbols and Declare Winner
    # "Play Again" or "Quit": Perform Appropriate Action
    while True:
        play_again == input('Would you like to play again? Y/N')
        if play_again.upper == 'N' or play_again.upper == 'Y':
            break
        else:
            print('Unexpected response. Please try again.')