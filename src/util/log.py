import datetime
from termcolor import colored
from util.parsearg import PasrseArg


class Log:

    _timeFormat = "%Y-%m-%d %H:%M:%S"

    def __init__(self):
        args = PasrseArg()
        self.file_source = args.get_log_file()
        self.log = args.get_log_mode()
        self.output = args.get_output_mode()

        self.file = open(self.file_source, "w")

    def transform(self, message, tag, type):
        return "{time} [{tag}] {type}: {message}".format(time=datetime.datetime.now().strftime(self._timeFormat), tag=tag.upper(), type=type, message=message)

    def error(self, message, tag="ficsbot"):
        _msg = self.transform(message, tag, colored("Error", "red"))
        if self.output is not "quiet":
            print _msg

        if self.log:
            self.file.write(_msg)

    def warn(self, message, tag="ficsbot"):
        _msg = self.transform(message, tag, colored("Warn", "yellow"))
        if self.output is "verbose":
            print _msg

        if self.log:
            self.file.write(_msg)

    def info(self, message, tag="ficsbot"):
        _msg = self.transform(message, tag, colored("Info", "blue"))
        if self.output is "verbose":
            print _msg

        if self.log:
            self.file.write(_msg)

    def close(self):
        self.file.close()