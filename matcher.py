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
        for i, card in enumerate(self.all_cards):
            for j, common in enumerate(self.all_cards):
                if card == common:
                    return True
        return False

    def if_two_pair(self):
        pairs_found = 0
        for i, card in enumerate(self.all_cards):
            for j, common in enumerate(self.all_cards):
                if card == common:
                    pairs_found += 1
        if pairs_found >= 2:
            return True
        return False

    def if_drill(self):
        same_rank_found = 0
        for i, card in enumerate(self.all_cards):
            for j, common in enumerate(self.all_cards):
                if card == common:
                    same_rank_found += 1
        if same_rank_found >= 3:
            return True
        return False

    def find_match(self):
        if self.if_drill():
            return 3
        if self.if_two_pair():
            return 2
        if self.if_pair():
            return 1
        return 0
