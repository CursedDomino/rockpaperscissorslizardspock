import sign
class Spock(sign.Sign):
    def __init__(self):
        sign.Sign.__init__(self)
        self.defeats = ['Scissors', 'Rock']
        self.defeated_by = ['Paper', 'Lizard']
        self.draws = ['Spock']