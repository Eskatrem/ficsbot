from util.log import Log
from loaders.configLoader import ConfigLoader


class Controller:
    def __init__(self):
        self.log = Log()
        conf_loader = ConfigLoader()
        self.lists = conf_loader.get_lists()
        self.help = conf_loader.get_help()
        self.help_lists = conf_loader.get_list_help()
        self.help_commands = conf_loader.get_command_help()

    def execute(self, command, arg, user, telnet):
        getattr(self, command)(arg, user, telnet)
