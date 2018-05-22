import matcher as cards_matcher


class Player:
    VERSION = "Texas Ranger 0.5"

    def __init__(self):
        self.me, self.card1, self.card2, self.value = None, None, None, None
        self.score = 0
        self.cards = None
        self.matcher = None

    def get_cards(self, game_state):
        self.cards = game_state["community_cards"]
        for player in game_state["players"]:
            if player["name"] == "Texas Rangers":  # this is us
                self.me = player
                self.card1 = self.me["hole_cards"][0]
                self.card2 = self.me["hole_cards"][1]

                self.score += self.card1
                self.score += self.card2

        self.matcher = cards_matcher.Matcher(self.cards, self.card1, self.card2)
        self.matcher.print_all()


    def betRequest(self, game_state):
        try:
            return 0
            self.value = game_state["current_buy_in"]

            self.get_cards(game_state)

            if game_state["round"] == 0:
                if self.matcher.if_pair([self.card1, self.card2]):
                    self.score *= 1.1
                self.value += 20
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
            print IOError
            return game_state["current_buy_in"]

    def pair_action(self):
        self.value += 20

    def all_in_action(self):
        self.value = 10000

    def showdown(self, game_state):
        pass
