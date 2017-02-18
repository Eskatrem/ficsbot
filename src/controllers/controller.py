from docopt import docopt
from util.log import Log


class Controller:
    def __init__(self, log=Log()):
        self.log = log

    def execute(self, command, arg, user, lists, log, telnet):
        getattr(self, command)(arg, user, lists, log, telnet)
