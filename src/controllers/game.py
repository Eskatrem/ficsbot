class game:

    def execute(self, command, arg, user):
        getattr(self, command)(arg=arg, user=user)

    def join(self, arg, user):
        print("{0} wants to join".format(user))

    def leave(self, arg, user):
        print("{0} wants to leave".format(user))

    def vote(self, arg, user):
        print("{0} voted {1}".format(user, arg))
