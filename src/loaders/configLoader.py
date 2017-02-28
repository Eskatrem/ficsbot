"""
--- Fics Bot {version} ---
- Made by schachbjm, Kevin Schaefer and Jonas Drotleff

Usage:
    tell {channel} /command [args]

{commands}

{lists}
"""

import yaml
from loaders.version import version
from util.command import Command
from util.list import List
from util.log import Log
from util.parsearg import PasrseArg


class ConfigLoader:
    def __init__(self, ):
        args = PasrseArg()
        self.file = args.get_config_file()
        self.config = None
        self.commands = {}
        self.lists = {}
        self.pref = {}
        self.valid = False
        self.log = Log()

        with open(self.file) as stream:
            try:
                self.config = yaml.load(stream)
            except yaml.YAMLError as exc:
                print str(exc)

        self.validate()

    def get_commands(self):
        if not self.valid:
            return

        _commands = self.config.get("commands")

        for _command in _commands:
            _key = _command.get("key")
            _controller = _command.get("controller")
            _restriction = _command.get("restriction")
            _description = _command.get("descritpion")
            _args = _command.get("argRequired")
            self.commands[_key] = Command(_key, _controller, _args, description=_description, restriction=_restriction)

        return self.commands

    def get_lists(self):
        if not self.valid:
            return

        _lists = self.config.get("lists")

        for _list in _lists:
            _key = _list.get("key")
            _listid = _list.get("listid")
            _description = _list.get("description")
            self.lists[_key] = List(_key, _listid, description=_description)

        return self.lists

    def get_channel(self):
        if not self.valid:
            return

        _pref = self.config.get("preferences")
        return _pref.get("channel")

    def get_user(self):
        if not self.valid:
            return

        _pref = self.config.get("preferences")
        _user = {}
        _user["name"] = _pref.get("user")
        _user["password"] = _pref.get("password")
        return _user

    def get_command_help(self):
        if not self.valid:
            return

        cmd_keys = []
        cmd_descriptions = []
        commands = "Commands:\n"
        _commands = self.config.get("commands")
        for _command in _commands:
            cmd_keys.append(_command.get("key"))
            cmd_descriptions.append(_command.get("description"))

        _space_length = len(max(cmd_keys, key=len)) + 4

        for i in xrange(len(cmd_keys)):
            key = cmd_keys[i]
            space = _space_length - len(key)
            desc = cmd_descriptions[i]
            commands += "    {key}{space}{description}\n".format(key=key, space=space, description=desc)

        return commands

    def get_list_help(self):
        if not self.valid:
            return

        list_keys = []
        list_descriptions = []
        lists = "Lists:\n"
        _lists = self.config.get("commands")
        for _list in _lists:
            list_keys.append(_list.get("key"))
            list_descriptions.append(_list.get("description"))

        _space_length = len(max(list_keys, key=len)) + 4

        for i in xrange(len(list_keys)):
            key = list_keys[i]
            space = _space_length - len(key)
            desc = list_descriptions[i]
            lists += "    {key}{space}{description}\n".format(key=key, space=space, description=desc)

    def get_help(self):
        if not self.valid:
            return

        _help = __doc__
        _help.format(version=version(),
                     channel=self.get_channel(),
                     commands=self.get_command_help(),
                     lists=self.get_list_help())
        return _help

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

            if "channel" not in _preferences:
                raise Exception("Missing channel.")

        self.valid = True
        return self.valid
