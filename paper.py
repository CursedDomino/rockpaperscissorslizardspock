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
                print('''"You may be strong, but your strategy is lacking. You were outmatched."''')
                print("Paper(Player) has covered Rock(Computer). The Player Wins!")
            else:
                print('''"I was expecting more from you. It seems you have a lot to learn."''')
                print("Paper(Player) has disproven Spock(Computer). The Player Wins!")
        elif self.determine_winner(cpu_symbol) == 'The Computer Wins!':
            if cpu_symbol.draws[0] == 'Scissors':
                print('''"You fought smart, but your wit was no match for my skill in the blade."''')
                print("Scissors(Computer) has sliced Paper(Player). The Computer Wins!")
            else:
                print('''"Lots of big words, no strength, lost focus. You made for a good snack."''')
                print("Lizard(Computer) has eaten Paper(Player). The Computer Wins!")
        else:
            print('''"At long last. I've been looking for someone who could rival my intellect."''')
            print('''Both players chose Paper. It's a draw!''')