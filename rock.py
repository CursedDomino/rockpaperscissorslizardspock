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
                print('''"You've been crushed. You're finished."''')
                print("Rock(Player) has crushed Scissors(Computer). The Player Wins!")
            else:
                print('''"You've been crushed. You're finished."''')
                print("Rock(Player) has crushed Lizard(Computer) The Player Wins!")
        elif self.determine_winner(cpu_symbol) == 'The Computer Wins!':
            if self.draws[0] == 'Scissors':
                print('''"You've been crushed. You're finished."''')
                print("Rock(Computer) has crushed Scissors(Player). The Computer Wins!")
            else:
                print('''"You've been crushed. You're finished."''')
                print("Rock(Computer) has crushed Lizard(Player) The Computer Wins!")