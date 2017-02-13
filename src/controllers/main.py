class main:
    def execute(self, command, arg, user):
        getattr(self, command)(arg=arg, user=user)

    def help(self, arg, user):
        print("asked for help?")

    def commands(self, arg, user):
        # TODO read from config.yaml
        print("list all commands")

    def list(self, arg, user):
        if not bool(user):
            user = "all"
        if not bool(arg):
            print("Provide a listname (e.x. captain)")
        else:
            # TODO get list from config.yaml
            print("tell {1} ={2}".format(user, arg))