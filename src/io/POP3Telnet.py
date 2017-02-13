import telnetlib


class POP3Telnet:
    def __init__(self, host, port):
        self.tel = telnetlib.Telnet(host, port)
        print("[Telnet]: Connected!")

    def close(self):
        self.tel.close()

    def read_data(self):
        return self.tel.read_some()

    def read_data2(self):
        return self.tel.read_very_eager()

    def command(self, com):
        self.tel.write("{}\r\n".format(com).encode())
        return self.read_data()

    def login(self, user, password):
        print("[Telnet]: Logging in as {}".format(user))
        self.tel.read_until(b"login: ")
        self.tel.write(user.encode('ascii') + b"\n")
        self.tel.write(password.encode('ascii') + b"\n")
        print("[Telnet]: Logged in!")
