import sign
class Spock(sign.Sign):
    def __init__(self, defeats, defeated_by, draws):
        sign.Sign.__init__(self)
        self.defeats = defeats
        self.defeated_by = defeated_by
        self.draws = draws

    def winning_line(self, cpu_symbol):
        if self.determine_winner(cpu_symbol) == 'The Player Wins!':
            if cpu_symbol.draws[0] == 'Rock':
                print('''"It seems your tough skin was no match for my futuristic abilities. What a shame."''')
                print("Spock(Player) has vaporized Rock(Computer). The Player Wins!")
            else:
                print('''"You are quite skilled, but your weapons are too old fashioned for me."''')
                print("Spock(Player) has smashed Scissors(Computer). The Player Wins!")
        elif self.determine_winner(cpu_symbol) == 'The Computer Wins!':
            if cpu_symbol.draws[0] == 'Paper':
                print('''"I was expecting more from you. It seems you have a lot to learn."''')
                print("Paper(Computer) has disproven Spock(Player). The Computer Wins!")
            else:
                print('''"Futuristic..strange. My poison was..very effective."''')
                print("Lizard(Computer) has poisoned Spock(Player). The Computer Wins!")
        else:
            print('''"Ah, so there was some talent among this galaxy after all."''')
            print('''Both players chose Spock. It's a draw!''')