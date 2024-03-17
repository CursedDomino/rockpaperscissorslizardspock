class Sign():
    def __init__(self):
        self.defeats = []
        self.defeated_by = []
        self.draws = []

    def determine_winner(self, cpu_symbol):
        if cpu_symbol.draws[0] in self.defeats:
            return 'The Player Wins!'
        elif cpu_symbol.draws[0] in self.defeated_by:
            return 'The Computer Wins!'
        else:
            return 'A Draw!'