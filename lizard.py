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
                print('''"Lots of big words..no strength..lost focus. You made for a good snack."''')
                print("Lizard(Player) has eaten Paper(Computer). The Player Wins!")
            else:
                print('''"Futuristic..strange. My poison was..very effective."''')
                print("Lizard(Player) has poisoned Spock(Computer). The Player Wins!")
        elif self.determine_winner(cpu_symbol) == 'The Computer Wins!':
            if cpu_symbol.draws[0] == 'Rock':
                print('''"Your abilities are no match for my strength! You've been crushed!"''')
                print("Rock(Computer) has crushed Lizard(Player). The Computer Wins!")
            else:
                print('''"I won't become your snack today. You made for good aiming practice."''')
                print("Scissors(Computer) has decapitated Lizard(Player). The Computer Wins!")
        else:
            print('''"Another..me? Evenly matched..it seems."''')
            print('''Both players chose Lizard. It's a draw!''')