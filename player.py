import json


class Player:
    VERSION = "Default Python folding player"

    def __init__(self):
        self.me, self.card1, self.card2 = None, None, None

    def betRequest(self, game_state):
        value = game_state["current_buy_in"]

        self.get_cards(game_state)

        for player in game_state["players"]:
            if player["name"] == "Texas Rangers":  # this is us

                if self.card1 == self.card2:
                    value = self.pair(value)

            print player["status"]

        if game_state["round"] == 0:
            return value + 20

        if value > 500:
            return 0

        return value + 2

    def get_cards(self, game_state):
        for player in game_state["players"]:
            if player["name"] == "Texas Rangers":  # this is us
                self.me = game_state["players"]
                self.card1 = self.me["hole_cards"][0]
                self.card2 = self.me["hole_cards"][1]

    def pair(self, value):
        value += 20
        return value

    def showdown(self, game_state):
        pass
