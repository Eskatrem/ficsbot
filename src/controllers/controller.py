from util.log import Log


class Controller:
    def __init__(self, log=Log()):
        self.log = log

    def execute(self, command, arg, user):
        getattr(self, command)(arg=arg, user=user)