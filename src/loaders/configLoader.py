import yaml
from util.command import Command
from util.list import List
from util.log import Log


class ConfigLoader:
    def __init__(self, file="config.yaml", log=Log()):
        self.file = file
        self.config = None
        self.commands = {}
        self.lists = {}
        self.pref = {}
        self.valid = False
        self.log = log

        with open(self.file) as stream:
            try:
                self.config = yaml.load(stream)
            except yaml.YAMLError as exc:
                print str(exc)

        self.validate()

    def getcommands(self):
        if not self.valid:
            return

        _commands = self.config.get("commands")

        for _command in _commands:
            _key = _command.get("key")
            _controller = _command.get("controller")
            _restriction = _command.get("restriction")
            _description = _command.get("descritpion")
            self.commands[_key] = Command(_key, _controller, description=_description, restriction=_restriction, log=self.log)

        return self.commands

    def getlists(self):
        if not self.valid:
            return

        _lists = self.config.get("lists")

        for _list in _lists:
            _key = _list.get("key")
            _listid = _list.get("listid")
            _description = _list.get("description")
            self.lists[_key] = List(_key, _listid, description=_description, log=self.log)

        return self.lists

    def validate(self):
        # standard format:
        # * indicates not obligatory items
        #
        # -------------
        #
        # commands:
        #   - command:
        #       key: "commandname"
        #       *restriction: "none|captain|..."
        #       controller: "class.function"
        #       *description: "description text"
        #   - ...
        #       ...
        #
        # lists:
        #   - list:
        #       key: "listname"
        #       listid: "FICS list identifier (e.x. noplay for =noplay)
        #       *description: "description text"
        #   - ...
        #       ...
        #
        # preferences:
        #   user: "ficsbot user name"
        #   password: "password for fics bot"

        if not bool(self.config):
            raise Exception("No configuaration loaded.")

        # Check for valid commands
        if "commands" not in self.config:
            raise Exception("Missing commands.")
        else:
            _commands = self.config.get("commands")
            for _command in _commands:

                if "key" not in _command:
                    raise Exception("Missing key of command.")
                elif " " in _command.get("key"):
                    raise Exception("Spaces are not allowed in key of command.")

                if "restriction" not in _command:
                    raise Exception("Missing restriction of command.")
                elif " " in _command.get("restriction"):
                    raise Exception("Spaces are not allowed in restriction of command.")

                if "controller" not in _command:
                    raise Exception("Missing controller of command.")
                elif " " in _command.get("controller"):
                    raise Exception("Spaces are not allowed in controller of command.")
                elif not len(_command.get("controller").split(".")) == 2:
                    raise Exception("Controller of command has to consist of 2 strings seperated by a dot.")

        # Check for valid lists
        if "lists" not in self.config:
            raise Exception("Missing lists.")
        else:
            _lists = self.config.get("lists")
            for _list in _lists:

                if "key" not in _list:
                    raise Exception("Missing key of list.")
                elif " " in _list.get("key"):
                    raise Exception("Spaces are not allowed in key of list.")

                if "listid" not in _list:
                    raise Exception("Missing list identifier of list.")
                elif " " in _list.get("listid"):
                    raise Exception("Spaces are not allowed in list identifier of list.")

        # Check for valid preferences
        if "preferences" not in self.config:
            raise Exception("Missing preferences.")
        else:
            _preferences = self.config.get("preferences")
            if "user" not in _preferences:
                raise Exception("Missing user name.")

            if "password" not in _preferences:
                raise Exception("Missing password of user.")

        self.valid = True
        return self.valid
