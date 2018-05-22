import json

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        for player in game_state["players"]:
            print player

        return 0

    def showdown(self, game_state):
        pass

