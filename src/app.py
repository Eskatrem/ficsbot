from loaders.configLoader import ConfigLoader


# set up logger
# TODO logger

# initial configuration load
configloader = ConfigLoader()
commands = configloader.getcommands()
lists = configloader.getlists()
