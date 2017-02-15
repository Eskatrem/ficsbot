import datetime


class Log:

    _timeFormat = "%Y-%m-%d %H:%M:%S"

    def __init__(self, file_source="ficsbot.log", quiet=False, verbose=False, quiet_out=False):
        self.file_source = file_source
        self.quiet = quiet
        self.verbose = verbose
        self.quiet_out = quiet_out

        if self.quiet and self.verbose:
            self.quiet = False

        self.file = open(self.file_source, "w")

    def transform(self, message, tag, type):
        return "{time} [{tag}] {type}: {message}".format(time=datetime.datetime.now().strftime(self._timeFormat), tag=tag.upper(), type=type, message=message)

    def error(self, message, tag="ficsbot"):
        _msg = self.transform(message, tag, "Error")
        if not self.quiet:
            print _msg

        if not self.quiet_out:
            self.file.write(_msg)

    def warn(self, message, tag="ficsbot"):
        _msg = self.transform(message, tag, "Warn")
        if not self.quiet:
            print _msg

        if not self.quiet_out:
            self.file.write(_msg)

    def info(self, message, tag="ficsbot"):
        _msg = self.transform(message, tag, "Info")
        if not self.quiet and self.verbose:
            print _msg

        if not self.quiet_out:
            self.file.write(_msg)

    def close(self):
        self.file.close()