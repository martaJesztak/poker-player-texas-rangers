import json


class Player:
    VERSION = "Default Python folding player"

    def __init__(self):
        self.me, self.card1, self.card2, self.bet = None, None, None, None

    def get_cards(self, game_state):
        for player in game_state["players"]:
            if player["name"] == "Texas Rangers":  # this is us
                self.me = player
                self.card1 = self.me["hole_cards"][0]
                self.card2 = self.me["hole_cards"][1]

    def betRequest(self, game_state):
        self.bet = game_state["current_buy_in"]

        self.get_cards(game_state)

        value = self.if_pair(value)

        if game_state["round"] == 0:
            return value + 20
        elif game_state["round"] == 1:
            pass
        elif game_state["round"] == 2:
            pass
        elif game_state["round"] == 3:
            pass
        else:
            pass

        if value > 500:
            return 0

        return value + 2

    def if_pair(self, value):
        if self.card1 == self.card2:
            value = self.pair(value)
        return value

    def pair(self, value):
        value += 20
        return value

    def showdown(self, game_state):
        pass
