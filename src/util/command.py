import importlib


class Command:

    def __init__(self, key, controller, description, restriction = "none"):
        self.key = key
        self.controller = controller
        self.description = description
        self.restriction = restriction

        _controllerDir = self.controller.split(".")
        _moduleName = _controllerDir[0]
        self.controllerName = _controllerDir[1]
        _module = importlib.import_module("controllers.{0}".format(_moduleName))
        self.controllerClass = getattr(_module, _moduleName)()

    def execute(self, arg=None, user=None):
        self.controllerClass.execute(self.controllerName, arg, user)