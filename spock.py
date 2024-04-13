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
                print('''Hmph. You're too modern for me. I'm in a whole different universe than you.''')
                print("Spock(Player) has vaporized Rock(Computer). The Player Wins!")
            else:
                print('''Hmph. You're too modern for me. I'm in a whole different universe than you.''')
                print("Spock(Player) has smashed Scissors(Computer). The Player Wins!")
        elif self.determine_winner(cpu_symbol) == 'The Computer Wins!':
            if cpu_symbol.draws[0] == 'Rock':
                print('''Hmph. You're too modern for me. I'm in a whole different universe than you.''')
                print("Spock(Computer) has vaporized Rock(Player). The Computer Wins!")
            else:
                print('''Hmph. You're too modern for me. I'm in a whole different universe than you.''')
                print("Spock(Computer) has smashed Scissors(Player). The Computer Wins!")
        else:
            print('''Ah, so there was some talent among this planet after all.''')
            print('''Both players chose Spock. It's a draw!''')