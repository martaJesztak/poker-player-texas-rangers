import json

class Player:
    VERSION = "Default Python folding player"

    def betRequest(self, game_state):
        for card in game_state["players"]["hole_cards"]:
            print card

        return 0

    def showdown(self, game_state):
        pass

