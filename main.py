from commands import *
from exception import CommandError


def main():
    print("% cssh")

    userCommand = getCommandFromUSer()

    while userCommand[0] != "exit":
        runCommand(userCommand)
        userCommand = getCommandFromUSer()

    print("%")


def runCommand(currentCommand):
    commandListe = ["ls", "pwd", "cat", "cd", "curl"]
    userCommand = currentCommand.split()
    isPipelinedCommand = "|" in currentCommand
    try:
        if isPipelinedCommand:
            print(run_pipeline(currentCommand))

        if userCommand[0] == "ls" and not isPipelinedCommand:
            ls(getNbArgs(userCommand=userCommand))

        if userCommand[0] == "pwd" and not isPipelinedCommand:
            pwd(getNbArgs(userCommand=userCommand))

        if userCommand[0] == "cat" and not isPipelinedCommand:
            if len(userCommand) == 2:
                cat(userCommand[1], getNbArgs(userCommand=userCommand))
            else:
                raise ArgumentError(1, getNbArgs(userCommand=userCommand))

        if userCommand[0] == "cd" and not isPipelinedCommand:
            if len(userCommand) == 2:
                cd(userCommand[1], getNbArgs(userCommand=userCommand))
            else:
                raise ArgumentError(1, getNbArgs(userCommand=userCommand))

        if userCommand[0] == "curl" and not isPipelinedCommand:
            if len(userCommand) == 4:
                curl(
                    userCommand[1],
                    userCommand[2],
                    userCommand[3],
                    getNbArgs(userCommand=userCommand),
                )
            else:
                raise ArgumentError(1, getNbArgs(userCommand=userCommand))

        if userCommand[0] not in commandListe:
            execute_single_command(currentCommand)

    except CommandError as e:
        print("Error: ", e)

    except ArgumentError as e:
        print("Error: ", e)


def getCommandFromUSer():
    userCommand = input("ccsh> ")
    return userCommand


def getNbArgs(userCommand):
    return len(userCommand) - 1


if __name__ == "__main__":
    main()
