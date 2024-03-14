class Symbol():
    def __init__(self):
        self.defeats = []
        self.defeated_by = []
        self.draws = []

    def determine_winner(self, cpu_symbol):
        if cpu_symbol in self.defeats:
            return 'Win'
        elif cpu_symbol in self.defeated_by:
            return 'Lose'
        else:
            return 'Draw'