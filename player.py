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
        self.value = game_state["current_buy_in"]

        self.get_cards(game_state)

        self.if_pair()

        if game_state["round"] == 0:
            return self.value + 20
        elif game_state["round"] == 1:
            pass
        elif game_state["round"] == 2:
            pass
        elif game_state["round"] == 3:
            pass
        else:
            pass

        if self.value > 500:
            return 0

        return self.value + 2

    def if_pair(self):
        if self.card1 == self.card2:
            self.value = self.pair_action()

    def pair_action(self):
        self.value += 20
        return self.value

    def showdown(self, game_state):
        pass
