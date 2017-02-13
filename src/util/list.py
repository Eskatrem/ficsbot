class List:

    def __init__(self, key, list, description=None):
        self.key = key
        self.list = list
        self.description = description
        if not bool(self.description):
            self.description = "List of all".format(key)

    def getPlayers(self):
        self.players = {}
