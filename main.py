import sign
import rock
import paper
import scissors
import lizard
import spock

import random

play_again = 'Y'
skip = False

player_score = 0
cpu_score = 0
draws = 0


while play_again.upper() == 'Y':
    player = 'None'
    computer = 'None'
    explain = 'N'
    while_loop = True


    # Rules Explained

    while while_loop == True and skip == False:
        explain = input('Would you like an explanation of the rules? Y/N: ')
        if explain.upper() == 'Y':
            print('')
            print('Rules:')
            print('The rules of the game are simple. Similar to rock paper scissors, you just have to choose a symbol to throw out.')
            print('Each symbol is weak to two and strong against two. If you throw out a symbol that is strong against your opponents, you win.')
            print('If you throw out a symbol that is weak against your opponents, you lose. If you throw out the same symbol, you draw. \n')
            print('Symbols:')
            print('Rock (Defeats Scissors and Lizard --- Defeated by Paper and Spock)')
            print('Paper (Defeats Rock and Spock --- Defeated by Scissors and Lizard)')
            print('Scissors (Defeats Paper and Lizard --- Defeated by Rock and Spock)')
            print('Lizard (Defeats Paper and Spock --- Defeated by Rock and Scissors)')
            print('Spock (Defeats Rock and Scissors --- Defeated by Paper and Lizard) \n')
            while_loop = False
        elif explain.upper() == 'N':
            print('The game will now begin. Good luck! \n')
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

    while True:
        player = input('Choose Your Symbol: Rock, Paper, Scissors, Lizard, Spock (Capitalization Does Not Matter) ').upper()
        if player == 'ROCK':
            player = rock.Rock(['Scissors', 'Lizard'], ['Paper', 'Spock'], ['Rock'])
            break
        elif player == 'PAPER':
            player = paper.Paper(['Rock', 'Spock'], ['Scissors', 'Lizard'], ['Paper'])
            break
        elif player == 'SCISSORS':
            player = scissors.Scissors(['Paper', 'Lizard'], ['Rock', 'Spock'], ['Scissors'])
            break
        elif player == 'LIZARD':
            player = lizard.Lizard(['Spock', 'Paper'], ['Rock', 'Scissors'], ['Lizard'])
            break
        elif player == 'SPOCK':
            player = spock.Spock(['Scissors', 'Rock'], ['Paper', 'Lizard'], ['Spock'])
            break
        else:
            print('Unexpected response. Please try again.')

    # Show Symbols and Declare Winner
    print('')
    print(f'. . . And the result is . . . ')
    player.winning_line(computer)
    print('')
    # "Play Again" or "Quit": Perform Appropriate Action
    while_loop = True

    if player.determine_winner(computer) == 'The Player Wins!':
        player_score +=1
    elif player.determine_winner(computer) == 'The Computer Wins!':
        cpu_score += 1
    else:
        draws +=1

    print('Scoreboard:')
    print(f'Player Victories: {player_score} \nComputer Victories: {cpu_score} \nDraws: {draws} \n')

    while while_loop == True:

        x = input('Would you like to play again? Y/N: ')

        if x.upper() == 'Y' and skip == False:
            x = input('Would you like to skip the rules from now on? Y/N: ')
            if x.upper() == 'Y':
                print('Understood. Rules will now be skipped.')
                print('Restarting...Good Luck! \n')
                skip = True
                while_loop = False
            else:
                print('Understood. Rules will continue being an option.')
                print('Restarting...Good Luck! \n')
                while_loop = False
        elif x.upper() == 'Y':
            print('Restarting...Good Luck! \n')
            while_loop = False
        elif x.upper() == 'N':
            print('Thanks for playing! \n')
            while_loop = False
            play_again = 'N'
        else:
            print('Unexpected response. Please try again. \n')