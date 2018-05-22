import json

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        print json.load(game_state)
        return 0

    def showdown(self, game_state):
        pass

