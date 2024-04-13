import sign
class Lizard(sign.Sign):
    def __init__(self, defeats, defeated_by, draws):
        sign.Sign.__init__(self)
        self.defeats = defeats
        self.defeated_by = defeated_by
        self.draws = draws

    def winning_line(self, cpu_symbol):
        if self.determine_winner(cpu_symbol) == 'The Player Wins!':
            if cpu_symbol.draws[0] == 'Paper':
                print('''This was fun! You made for a pretty good snack!''')
                print("Lizard(Player) has eaten Paper(Computer). The Player Wins!")
            else:
                print('''This was fun! You'll make for a pretty good snack later!''')
                print("Lizard(Player) has poisoned Spock(Computer). The Player Wins!")
        elif self.determine_winner(cpu_symbol) == 'The Computer Wins!':
            if self.draws[0] == 'Paper':
                print('''This was fun! You made for a pretty good snack!''')
                print("Lizard(Computer) has eaten Paper(Player). The Computer Wins!")
            else:
                print('''This was fun! You'll make for a pretty good snack later!''')
                print("Lizard(Computer) has poisoned Spock(Player). The Computer Wins!")
        else:
            print('''Haha! That was fun! Again, again!''')
            print('''Both players chose Lizard. It's a draw!''')