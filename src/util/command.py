import importlib
from util.log import Log


class Command:
    def __init__(self, key, controller, req_args=False, description="No description provided.", restriction="none"):
        self.key = key
        self.log = Log()
        self.req_args = req_args
        self.controller = controller
        self.description = description
        self.restriction = restriction

        _controller_dir = self.controller.split(".")
        _module_name = _controller_dir[0]
        self.controller_name = _controller_dir[1]
        _module = importlib.import_module("controllers.{0}".format(_module_name))
        self.controller_class = getattr(_module, _module_name.capitalize())()

    def execute(self, user, telnet, lists, arg=None):

        if "none" not in self.restriction:
            if user not in self.lists[self.restriction].get_users(telnet):
                self.log.warn("{user} called {cmd} without permission (restricted by role)".format(user=user, cmd=self.controller_name), tag="command")
                return

        if self.req_args and not bool(arg):
            self.log.warn("{user} called {cmd} which requires arguments".format(user=user, cmd=self.controller_name), tag="command")
            return

        self.controller_class.execute(self.controller_name, arg, user, telnet)
