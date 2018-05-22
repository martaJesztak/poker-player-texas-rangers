import json


class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        value = game_state["current_buy_in"]

        for player in game_state["players"]:
            if player["name"] == "Texas Rangers":  # this is us

                if player["hole_cards"][0]["rank"] == player["hole_cards"][1]["rank"]:
                    value += 20

            print player["status"]

        if game_state["round"] == 0:
            return value + 20
        return value + 2

    def showdown(self, game_state):
        pass
