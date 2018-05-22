import json

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        for player in game_state["players"]:
            if player["name"] == "Texas Rangers":
                for card in player["hole_cards"]:
                    print card

        if game_state["round"] == 0:
            return 50
        return game_state["current_buy_in"] + 2

    def showdown(self, game_state):
        pass

