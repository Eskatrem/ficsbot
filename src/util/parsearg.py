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
import sys
import argparse


class PasrseArg:
    def __init__(self):
        self.arg = sys.argv
        self.parser = argparse.ArgumentParser(description=__doc__)

        self.parser.add_argument("-h", "--help", action=)
        self.parser.add_argument("--config", action="store", dest="config", type=str, default="config.yaml")
