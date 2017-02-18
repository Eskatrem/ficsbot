class List:

    def __init__(self, key, listid, log, description="No description provided."):
        self.key = key
        self.listid = listid
        self.log = log
        self.description = description
        self.user = {}

    def getusers(self, telnet):
        telnet.command("={listid}".format(listid=self.listid))
        data = telnet.readuntil("-- {listid} list:".format(listid=self.listid))
        data = telnet.readuntil("\n")
        data = telnet.readuntil("fics").replace("\n", " ").replace("\r", " ").replace("fics","").split(" ")
        data = filter(None, data)
        self.user = data
        return self.user

    def adduser(self, user, telnet):
        if " " not in user and user:
            telnet.write("+{listid} {user}".format(listid=self.listid, user=user))
            self.user.add(user)
