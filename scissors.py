import symbol
class Scissors(symbol.Symbol):
    def __init__(self):
        symbol.Symbol.__init__(self)
        self.defeats = ['Paper', 'Lizard']
        self.defeated_by = ['Rock', 'Spock']
        self.draws = ['Scissors']