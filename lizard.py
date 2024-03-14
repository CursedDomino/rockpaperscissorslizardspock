import symbol
class Lizard(symbol.Symbol):
    def __init__(self):
        symbol.Symbol.__init__(self)
        self.defeats = ['Spock', 'Paper']
        self.defeated_by = ['Rock', 'Scissors']
        self.draws = ['Lizard']