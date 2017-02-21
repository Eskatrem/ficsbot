from controllers.controller import Controller


class Game(Controller):
    @staticmethod
    def join(self, arg, user, lists, log, telnet):
        lists.add_user(user, telnet)
        telnet.write("tell {0} You have joined the team. Type /help for more information.".format(user))
        log.info("{0} joined".format(user), "game.join")

    @staticmethod
    def leave(arg, user, lists, log, telnet):
        lists.add_user(user)
        telnet.write("tell {0} You have joined the team. Type /help for more information.".format(user))
        log.info("{0} left".format(user), "game.leave")

    @staticmethod
    def vote(self, arg, user, lists, log, telnet):
        log.info("{0} voted for {1}".format(user, arg[0]), "game.vote")
