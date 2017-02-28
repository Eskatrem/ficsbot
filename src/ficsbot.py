from io.POP3Telnet import POP3Telnet
from loaders.configLoader import ConfigLoader
from util.log import Log
from util.parsearg import PasrseArg


PasrseArg()
log = Log()
configLoader = ConfigLoader()
lists = configLoader.get_lists()
user = configLoader.get_user()
telnet = POP3Telnet("freechess.org", 5000)
telnet.login(user["name"], user["password"])

lists = configLoader.get_lists()
commands = configLoader.get_commands()

while True:
    data = telnet.read_line().split("({channel}): /".format(channel=configLoader.get_channel()))

    if data[1:]:
        _user = data[0].replace("\r", "").replace("\n", "")
        _msg = data[1].replace("\r", "").replace("\n", "").split(" ")
        _cmd = _msg[0]
        _arg = _msg[1:]

        if _cmd is "quit" and _user in lists["captain"]:
            break

        if _cmd in commands:
            commands[_cmd].execute(_user, telnet, lists, arg=_arg)
