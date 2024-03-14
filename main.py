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

    # Start Game
    # Explain Rules
    while True:
        explain = input('Would you like an explanation of the rules? Y/N')
        if explain.upper() == 'Y':
            pass
            # Print Rules Here
        elif explain.upper() == 'N':
            print('The game will now begin. Good luck!')
        else:
            print('Unexpected response. Please try again.')

    # Com
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