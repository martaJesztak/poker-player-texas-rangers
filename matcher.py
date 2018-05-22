class Matcher:

    def __init__(self, cards, card1, card2):
        self.cards = cards
        self.card1 = card1
        self.card2 = card2

    def print_all(self):
        print self.cards

    def if_pair(self, cards):
        for i, card in enumerate(cards):
            for j, other in enumerate(cards):
                if card == other:
                    return True
        return False
