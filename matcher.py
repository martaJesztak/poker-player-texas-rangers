class Matcher:

    def __init__(self, cards, common_cards, player):
        self.cards = cards
        self.common_cards = common_cards
        self.all_cards = cards + common_cards
        self.print_all()
        self.player = player

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

    def if_straight(self):
        for i, card in enumerate(self.all_cards):
            for j, common in enumerate(self.all_cards):
                if self.get_rank_value(card) + 1 == self.get_rank_value(common):
                    # not actual drill
                    return True
        return False

    def if_flush(self):
        same_suit = 0
        for i, card in enumerate(self.all_cards):
            for j, common in enumerate(self.all_cards):
                if card["suit"] == common["suit"]:
                    same_suit += 1
                if same_suit > 4:
                    return True
        return False

    def if_poker(self):
        same_rank_found = 0
        for i, card in enumerate(self.all_cards):
            for j, common in enumerate(self.all_cards):
                if card == common:
                    same_rank_found += 1
        if same_rank_found >= 4:
            return True
        return False

    def find_match(self):
        if self.if_poker():
            return 10000
        if self.if_flush():
            return 6
        if self.if_straight():
            return 5
        if self.if_drill():
            return 3
        if self.if_two_pair():
            return 2
        if self.if_pair():
            return 1
        return 0

    def get_rank_value(self, card):
        rank = card["rank"]
        try:
            return int(rank)
        except:
            if rank == "A":
                return 14
            if rank == "K":
                return 13
            if rank == "Q":
                return 12
            if rank == "J":
                return 11