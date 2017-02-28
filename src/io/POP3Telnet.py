import telnetlib
from util.log import Log


class POP3Telnet:
    def __init__(self, host, port):
        self.tel = telnetlib.Telnet(host, port)
        self.log = Log()
        self.log.info("Connected to {host} on port {port}".format(host=host, port=port), tag="TELNET")

    def close(self):
        self.tel.close()

    def read_line(self):
        return self.tel.read_until("\n")

    def write(self, msg):
        self.tel.write("{msg}\r\n".format(msg=msg).encode())

    def tell(self, whom, what):
        self.tel.write("tell {whom} {what}".format(whom=whom, what=what).encode())

    def login(self, user, password):
        self.tel.read_until(b"login: ")
        self.tel.write(user.encode('ascii') + b"\n")
        self.tel.write(password.encode('ascii') + b"\n")
        self.log.info("Logged in as {user}".format(user=user), tag="TELNET")