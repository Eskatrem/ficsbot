from controllers.controller import Controller


class Main(Controller):
    @staticmethod
    def help(self, arg, user, lists, log, telnet):
        telnet.tell(user, "")

    @staticmethod
    def commands(self, arg, user, lists, log, telnet):
        # TODO read from config.yaml
        print("list all commands")

    @staticmethod
    def list(self, arg, user, lists, log, telnet):
        if bool(arg):
            list = ", ".join(map(str, lists[arg[0]].get_users(telnet)))
            telnet.write("tell {user} {list}".format(user=user, list=list))
