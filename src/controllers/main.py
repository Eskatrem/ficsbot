from controllers.controller import Controller


class Main(Controller):
    def help(self, arg, user, lists, log, telnet):
        print("asked for help?")

    def commands(self, arg, user, lists, log, telnet):
        # TODO read from config.yaml
        print("list all commands")

    def list(self, arg, user, lists, log, telnet):
        if bool(arg):
            list = ", ".join(map(str, lists[arg[0]].getusers(telnet)))
            telnet.command("tell {user} {list}".format(user=user, list=list))
