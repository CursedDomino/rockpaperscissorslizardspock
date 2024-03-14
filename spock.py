import symbol
class Spock(symbol.Symbol):
    def __init__(self):
        symbol.Symbol.__init__(self)
        self.defeats = ['Scissors', 'Rock']
        self.defeated_by = ['Paper', 'Lizard']
        self.draws = ['Spock']