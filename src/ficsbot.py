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

from loaders.configLoader import ConfigLoader
from util.log import Log


# initialize docopt for argument parsing
args = docopt(__doc__, version="ficsbot 0.2")

log = Log(file_source=args["--out"], quiet=args["--quiet"], verbose=args["--verbose"], quiet_out=args["--no-output"])
# initial configuration load
configLoader = ConfigLoader(file=args["--config"] ,log=log)
commands = configLoader.getcommands()
lists = configLoader.getlists()
commands["join"].execute()