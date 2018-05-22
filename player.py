import json

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        for player in game_state["players"]:
            if player["name"] == "Texas Rangers":
                print player

        if game_state["round"] == 0:
            return 10
        return 1

    def showdown(self, game_state):
        pass

