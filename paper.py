import sign
class Paper(sign.Sign):
    def __init__(self):
        sign.Sign.__init__(self)
        self.defeats = ['Rock', 'Spock']
        self.defeated_by = ['Scissors', 'Lizard']
        self.draws = ['Paper']