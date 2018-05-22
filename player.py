import matcher as cards_matcher


class Player:
    VERSION = "Texas Ranger 0.5"

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

                self.score += self.cards[0]["rank"]  # TODO do when AKQJ
                self.score += self.cards[1]["rank"]  # TODO do when AKQJ

        self.matcher = cards_matcher.Matcher(self.cards, self.common_cards)

    def betRequest(self, game_state):
        try:
            self.value = game_state["current_buy_in"]

            self.get_cards(game_state)

            if game_state["round"] == 0:
                self.value += 10
                self.value *= self.matcher.find_match()
            elif game_state["round"] == 1:
                pass
            elif game_state["round"] == 2:
                pass
            elif game_state["round"] == 3:
                pass
            else:
                pass

            if game_state["current_buy_in"] >= self.me["stack"]:
                self.all_in_action()

            print self.value
            return self.value
        except IOError:
            return 0

    def pair_action(self):
        self.value += 20

    def all_in_action(self):
        self.value = 10000

    def showdown(self, game_state):
        pass
