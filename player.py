import matcher as cards_matcher
import math

class Player:
    VERSION = "yo mama so fat it crashed the poker"

    def __init__(self):
        self.me, self.card1, self.card2, self.value = None, None, None, None
        self.score = 0
        self.cards = None
        self.common_cards = None
        self.matcher = None

    def get_cards(self, game_state):
        self.common_cards = game_state["community_cards"]
        for player in game_state["players"]:
            if player["name"] == "Texas Rangers":  # this is us
                self.me = player
                self.cards = self.me["hole_cards"]

                self.score += self.get_rank_value(self.cards[0])
                self.score += self.get_rank_value(self.cards[1])

        self.matcher = cards_matcher.Matcher(self.cards, self.common_cards)

    def betRequest(self, game_state):
        try:
            self.value = game_state["current_buy_in"]

            self.get_cards(game_state)

            if game_state["round"] == 0:
                self.value += 10
                self.value *= self.matcher.find_match()
            elif game_state["round"] == 1:
                self.value *= self.matcher.find_match()
            elif game_state["round"] == 2:
                self.value *= self.matcher.find_match()
            elif game_state["round"] == 3:
                self.value *= self.matcher.find_match()


            if game_state["current_buy_in"] >= self.me["stack"]:
                self.all_in_action()

            print self.value
            return math.floor(self.value)
        except:
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

    def all_in_action(self):
        self.value = 10000

    def showdown(self, game_state):
        pass
