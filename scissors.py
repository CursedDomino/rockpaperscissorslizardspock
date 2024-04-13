import sign
class Scissors(sign.Sign):
    def __init__(self, defeats, defeated_by, draws):
        sign.Sign.__init__(self)
        self.defeats = defeats
        self.defeated_by = defeated_by
        self.draws = draws

    def winning_line(self, cpu_symbol):
        if self.determine_winner(cpu_symbol) == 'The Player Wins!':
            if cpu_symbol.draws[0] == 'Paper':
                print('''"You fight smart, but your wit was no match for my skill."''')
                print("Scissors(Player) has sliced Paper(Computer). The Player Wins!")
            else:
                print('''"I won't become your snack today. You made for good aiming practice."''')
                print("Scissors(Player) has decapitated Lizard(Computer). The Player Wins!")
        elif self.determine_winner(cpu_symbol) == 'The Computer Wins!':
            if cpu_symbol.draws[0] == 'Rock':
                print('''"You have talent, but your blades could never pierce my skin!"''')
                print("Rock(Computer) has crushed Scissors(Player). The Computer Wins!")
            else:
                print('''"You are quite skilled, but your weapons are too old fashioned for me."''')
                print("Spock(Computer) has smashed Scissors(Player). The Computer Wins!")
        else:
            print('''"Impressive. You truly know how to wield a blade."''')
            print('''Both players chose Scissors. It's a draw!''')

    # if self.draws[0] == 'Paper':
    #             print('''Sliced and diced. My blades can cut through anything.''')
    #             print("Scissors(Computer) has sliced Paper(Player). The Computer Wins!")
    #         else:
    #             print('''It was over before it began. My blades can cut through anything.''')
    #             print("Scissors(Computer) has decapitated Lizard(Player). The Computer Wins!")