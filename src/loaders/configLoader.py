import yaml
import importlib
from util.command import Command


class ConfigLoader:
    def __init__(self, file="config.yaml"):
        self.file = file
        self.config = None
        self.commands = {}
        self.pref = {}

        with open(self.file) as stream:
            try:
                self.config = yaml.load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def getcommands(self):
        if "commands" not in self.config:
            print("Could not find commands in {0}".format(self.file))
            return

        _commands = self.config.get("commands")

        for _command in _commands:
            _key = _command.get("key")
            _controller = _command.get("controller")
            _restriction = _command.get("restriction")
            _description = _command.get("descritpion")
            self.commands[_key] = Command(_key, _controller, _description, restriction=_restriction)

        return self.commands

    def validate(self):
        return True
