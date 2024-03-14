import symbol
class Rock(symbol):
    def __init__(self):
        symbol.Symbol.__init__(self)
        self.defeats = ['Scissors', 'Lizard']
        self.defeated_by = ['Paper', 'Spock']
        self.draws = ['Rock']

