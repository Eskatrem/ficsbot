class List:
    def __init__(self, key, listid, log, description="No description provided."):
        self.key = key
        self.listid = listid
        self.log = log
        self.description = description
        self.users = []

    def get_users(self, telnet):
        telnet.write("={listid}".format(listid=self.listid))
        data = telnet.readuntil("-- {listid} list:".format(listid=self.listid))
        data = telnet.readuntil("\n")
        data = telnet.readuntil("fics").replace("\n", " ").replace("\r", " ").replace("fics","").split(" ")
        data = filter(None, data)
        self.users = data
        return self.users

    def add_user(self, user, telnet):
        if " " not in user and user:
            telnet.write("+{listid} {user}".format(listid=self.listid, user=user))
            self.users.append(user)

    def remove_user(self, user, telnet):
        if " " not in user and user and user in self.users:
            telnet.write("-{listid} {user}".format(listid=self.listid, user=user))
            self.users.remove(user)