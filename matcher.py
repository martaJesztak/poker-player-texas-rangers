class Matcher:

    def __init__(self, cards, common_cards):
        self.cards = cards
        self.common_cards = common_cards
        self.all_cards = cards + common_cards
        self.print_all()

    def print_all(self):
        print self.cards
        print self.common_cards

    def if_pair(self):
        for i, card in enumerate(self.cards):
            for j, common in enumerate(self.common_cards):
                if card == common:
                    return True
        return False

    def find_match(self):
        if self.if_pair():
            return 1
        return 0
