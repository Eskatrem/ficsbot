from controllers.controller import Controller


class Game(Controller):
    def join(self, arg, user):
        self.log.info("{user} tries to join".format(user=user))

    def leave(self, arg, user):
        print("{0} wants to leave".format(user))

    def vote(self, arg, user):

        print("{0} voted {1}".format(user, arg))
