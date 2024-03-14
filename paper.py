import symbol
class Paper(symbol.Symbol):
    def __init__(self):
        symbol.Symbol.__init__(self)
        self.defeats = ['Rock', 'Spock']
        self.defeated_by = ['Scissors', 'Lizard']
        self.draws = ['Paper']