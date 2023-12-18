class CommandError(Exception):
    def __init__ (self, message="No such command"):
        self.message = message
        super().__init__(self.message)
