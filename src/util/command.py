import importlib
from util.log import Log


class Command:
    def __init__(self, key, controller, reqargs, description="No description provided.", restriction="none"):
        self.key = key
        self.reqArgs = reqargs
        self.controller = controller
        self.description = description
        self.restriction = restriction

        _controllerDir = self.controller.split(".")
        _moduleName = _controllerDir[0]
        self.controllerName = _controllerDir[1]
        _module = importlib.import_module("controllers.{0}".format(_moduleName))
        self.controllerClass = getattr(_module, _moduleName.capitalize())()

    def execute(self, user, log, lists, telnet, arg=None):
        if "none" not in self.restriction:
            if user not in lists[self.restriction].getusers(telnet):
                log.warn("{user} is not permitted to use {cmd}".format(user=user, cmd=self.controllerName), tag="command")
                return

        if self.reqArgs and not bool(arg):
            log.warn("{user} called {cmd} which requires arguments".format(user=user, cmd=self.controllerName), tag="command")
            return

        self.controllerClass.execute(self.controllerName, arg, user, lists, log, telnet)
