import sign
class Lizard(sign.Sign):
    def __init__(self):
        sign.Sign.__init__(self)
        self.defeats = ['Spock', 'Paper']
        self.defeated_by = ['Rock', 'Scissors']
        self.draws = ['Lizard']