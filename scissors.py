import sign
class Scissors(sign.Sign):
    def __init__(self):
        sign.Sign.__init__(self)
        self.defeats = ['Paper', 'Lizard']
        self.defeated_by = ['Rock', 'Spock']
        self.draws = ['Scissors']