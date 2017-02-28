def version():
    with open("VERSION") as stream:
        return stream.read()
