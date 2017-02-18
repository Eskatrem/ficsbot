import importlib
from util.log import Log


class Command:
    def __init__(self, key, controller, description="No description provided.", restriction="none", log=Log()):
        self.key = key
        self.controller = controller
        self.description = description
        self.restriction = restriction
        self.lists={}

        _controllerDir = self.controller.split(".")
        _moduleName = _controllerDir[0]
        self.controllerName = _controllerDir[1]
        _module = importlib.import_module("controllers.{0}".format(_moduleName))
        self.controllerClass = getattr(_module, _moduleName.capitalize())(log=log)

    def execute(self, arg=None, user=None):
        self.controllerClass.execute(self.controllerName, arg, user)