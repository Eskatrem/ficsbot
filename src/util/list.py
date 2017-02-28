from util.log import Log


class List:
    def __init__(self, key, list_id, description="No description provided."):
        self.key = key
        self.list_id = list_id
        self.log = Log()
        self.description = description
        self.users = []

    def get_users(self, telnet):
        telnet.write("={listid}".format(listid=self.list_id))
        data = telnet.readuntil("-- {listid} list:".format(listid=self.list_id))
        data = telnet.readuntil("\n")
        data = telnet.readuntil("fics").replace("\n", " ").replace("\r", " ").replace("fics","").split(" ")
        data = filter(None, data)
        self.users = data
        return self.users

    def add_user(self, user, telnet):
        if " " not in user and user:
            telnet.write("+{listid} {user}".format(listid=self.list_id, user=user))
            self.users.append(user)

    def remove_user(self, user, telnet):
        if " " not in user and user and user in self.users:
            telnet.write("-{listid} {user}".format(listid=self.list_id, user=user))
            self.users.remove(user)
