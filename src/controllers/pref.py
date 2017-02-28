from controllers.controller import Controller


class Pref(Controller):
    @staticmethod
    def addCaptain(self, arg, user, telnet):
        if bool(arg):
            self.lists["captain"].add_user(arg)
