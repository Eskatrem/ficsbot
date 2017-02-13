class List:

    def __init__(self, key, listid, description="No description provided."):
        self.key = key
        self.listid = listid
        self.description = description
        self.players = {}

    def getplayers(self):
        return self.players