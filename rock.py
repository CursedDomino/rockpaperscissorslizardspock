import sign
class Rock(sign.Sign):
    def __init__(self):
        sign.Sign.__init__(self)
        self.defeats = ['Scissors', 'Lizard']
        self.defeated_by = ['Paper', 'Spock']
        self.draws = ['Rock']

