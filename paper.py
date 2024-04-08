import sign
class Paper(sign.Sign):
    def __init__(self, defeats, defeated_by, draws):
        sign.Sign.__init__(self)
        self.defeats = defeats
        self.defeated_by = defeated_by
        self.draws = draws

    def winning_line(self, cpu_symbol):
        if self.determine_winner(cpu_symbol) == 'The Player Wins!':
            if cpu_symbol.draws[0] == 'Rock':
                print('''You never stood a chance. No one can match my wit.''')
                print("Paper(Player) has covered Rock(Computer). The Player Wins!")
            else:
                print('''You never stood a chance. No one can match my wit.''')
                print("Paper(Player) has disproven Spock(Computer). The Player Wins!")
        elif self.determine_winner(cpu_symbol) == 'The Computer Wins!':
            if self.draws[0] == 'Rock':
                print('''You never stood a chance. No one can match my wit.''')
                print("Paper(Computer) has covered Rock(Player). The Computer Wins!")
            else:
                print('''You never stood a chance. No one can match my wit.''')
                print("Paper(Computer) has disproven Spock(Player). The Computer Wins!")