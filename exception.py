class CommandError(Exception):
    def __init__ (self, message="Command Error: No such command"):
        self.message = message
        super().__init__(self.message)

class ArgumentError(Exception):
    def __init__ (self, expectedNbArgs, gotNbArgs ,message="Argument Error"):
        self.expectedNbArgs = expectedNbArgs
        self.gotNbArgs = gotNbArgs
        self.message = message + ": Expected " + str(expectedNbArgs) + " arguments and got " + str(gotNbArgs) 
        super().__init__(self.message)