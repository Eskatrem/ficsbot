from util.log import Log


class List:

    def __init__(self, key, listid, description="No description provided.", log=Log()):
        self.key = key
        self.listid = listid
        self.description = description
        self.players = {}

    def getplayers(self):
        return self.players