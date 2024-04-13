import sign
class Rock(sign.Sign):
    def __init__(self, defeats, defeated_by, draws):
        sign.Sign.__init__(self)
        self.defeats = defeats
        self.defeated_by = defeated_by
        self.draws = draws

    def winning_line(self, cpu_symbol):
        if self.determine_winner(cpu_symbol) == 'The Player Wins!':
            if cpu_symbol.draws[0] == 'Scissors':
                print('''"You have talent, but your blades could never pierce my skin!"''')
                print("Rock(Player) has crushed Scissors(Computer). The Player Wins!")
            else:
                print('''"Your abilities are no match for my strength! You've been crushed!"''')
                print("Rock(Player) has crushed Lizard(Computer). The Player Wins!")
        elif self.determine_winner(cpu_symbol) == 'The Computer Wins!':
            if cpu_symbol.draws[0] == 'Paper':
                print('''"You may be strong, but your intellect is lacking. You were outmatched."''')
                print("Paper(Computer) has covered Rock(Player). The Computer Wins!")
            else:
                print('''"It seems your tough skin was no match for my futuristic abilities. What a shame."''')
                print("Spock(Computer) has vaporized Rock(Player). The Computer Wins!")
        else:
            print('''"Not bad! It seems we're evenly matched."''')
            print('''Both players chose Rock. It's a draw!''')

    # if self.draws[0] == 'Scissors':
    #             print('''"You've been crushed. You're finished."''')
    #             print("Rock(Computer) has crushed Scissors(Player). The Computer Wins!")
    #         else:
    #             print('''"You've been crushed. You're finished."''')
    #             print("Rock(Computer) has crushed Lizard(Player). The Computer Wins!")