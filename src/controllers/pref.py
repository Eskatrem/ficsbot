from controllers.controller import Controller


class Pref(Controller):
    def execute(self, command, arg, user):
        getattr(self, command)(arg=arg, user=user)

    def addCaptain(self, arg, user):
        print("{0} wants to add {1} to captain list".format(user, arg))