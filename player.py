class Player:
    VERSION = "Default Python folding player"

    def __init__(self):
        self.me, self.card1, self.card2, self.value = None, None, None, None

    def get_cards(self, game_state):
        for player in game_state["players"]:
            if player["name"] == "Texas Rangers":  # this is us
                self.me = player
                self.card1 = self.me["hole_cards"][0]
                self.card2 = self.me["hole_cards"][1]

    def betRequest(self, game_state):
        try:
            self.value = game_state["current_buy_in"]

            self.get_cards(game_state)

            if game_state["round"] == 0:
                self.value += 20
            elif game_state["round"] == 1:
                pass
            elif game_state["round"] == 2:
                pass
            elif game_state["round"] == 3:
                pass
            else:
                pass

            print self.card1
            print self.card2
            if self.card1 == self.card2:
                self.pair_action()

            if game_state["current_buy_in"] >= self.me["stack"]:
                self.all_in_action()

            print self.value

            return self.value
        except IOError:
            return game_state["current_buy_in"]

    def pair_action(self):
        self.value += 20

    def all_in_action(self):
        self.value = 10000

    def showdown(self, game_state):
        pass
