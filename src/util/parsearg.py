import sys
import argparse
from loaders.version import version


class PasrseArg:
    def __init__(self):
        self.arg = sys.argv
        self.parser = argparse.ArgumentParser(description="Fics Bot")

        self.parser.add_argument("--log-file",
                                 action="store",
                                 dest="logfile",
                                 type=str,
                                 default="ficsbot.log",
                                 help="specify the log file")
        self.parser.add_argument("--no-log",
                                 "-l",
                                 action="store_false",
                                 default=True,
                                 dest="log",
                                 help="disable output in log file")
        self.parser.add_argument("--verbose",
                                 "-v",
                                 action="store_true",
                                 default=False,
                                 dest="verbose",
                                 help="print everything in console")
        self.parser.add_argument("--quiet",
                                 "-q",
                                 action="store_true",
                                 default=False,
                                 dest="quiet",
                                 help="print nothing in console")
        self.parser.add_argument("--config-file",
                                 action="store",
                                 dest="config",
                                 type=str,
                                 default="config.yaml",
                                 help="specify the configuration file")
        self.parser.add_argument("--version",
                                 action="version",
                                 version=version(),
                                 help="print version number")

        self.args = self.parser.parse_args()

    def get_output_mode(self):
        # returns output mode:
        # "normal" (standard) | "verbose" | "quiet"
        if self.args.quiet and self.args.verbose:
            return "normal"
        if self.args.quiet:
            return "quiet"
        if self.args.verbose:
            return "verbose"

        return "normal"

    def get_log_file(self):
        # returns string with log file path
        return self.args.logfile

    def get_log_mode(self):
        # returns whether a log file should be written
        return self.args.log

    def get_config_file(self):
        # returns string with config file path
        return self.args.config
