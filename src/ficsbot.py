"""
FICS Bot.

Usage:
  ./ficsbot
  ./ficsbot [--quiet | --verbose] [--out=<file> | --no-output] [--config=<file>]
  ./ficsbot [--config=<file>]
  ./ficsbot --help
  ./ficsbot --version

Options:
  -h --help        show this
  -v --version     print version number
  --out=<file>     specify log file [default: ficsbot.log]
  --no-output      do not print to log file
  -q --quiet       print less text
  -V --verbose     print more text
  --config=<file>  load specific config file [default: config.yaml]
"""

from docopt import docopt
from io.POP3Telnet import POP3Telnet
from loaders.configLoader import ConfigLoader
from util.log import Log
import sys


# initialize docopt for argument parsing
args = docopt(__doc__, version="ficsbot 0.2")
log = Log(file_source=args["--out"], quiet=args["--quiet"], verbose=args["--verbose"], quiet_out=args["--no-output"])
# initial configuration load
configLoader = ConfigLoader(log, file=args["--config"])

user = configLoader.getuser()
pop = POP3Telnet("freechess.org", 5000, log=log)
pop.login(user["name"], user["password"])

lists = configLoader.getlists()
commands = configLoader.getcommands()

while True:
    data = pop.readuntil("\n").split("(21): /")

    if data[1:]:
        _user = data[0].replace("\r", "").replace("\n", "")
        _msg = data[1].replace("\r", "").replace("\n", "").split(" ")
        _cmd = _msg[0]
        _arg = _msg[1:]

        if _cmd in commands:
           commands[_cmd].execute(_user, log, lists, pop, arg=_arg)
