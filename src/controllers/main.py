from controllers.controller import Controller


class Main(Controller):
    @staticmethod
    def help(self, arg, user, telnet):
        telnet.tell(user, self.help)

    @staticmethod
    def commands(self, arg, user, telnet):
        telnet.tell(user, self.help_commands)

    @staticmethod
    def lists(self, arg, user, telnet):
        telnet.tell(user, self.help_lists)

    @staticmethod
    def list(self, arg, user, telnet):
        if bool(arg):
            _list = ", ".join(map(str, self.lists[arg[0]].get_users(telnet)))
            telnet.write("tell {user} {list}".format(user=user, list=_list))
