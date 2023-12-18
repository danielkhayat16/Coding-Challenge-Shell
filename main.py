from commands import *
from exception import CommandError

def main():
    print('% cssh')
    commandListe = ["ls", "pwd", "cat"]
    userCommand = getCommandFromUSer()
    while(userCommand[0] != "exit"):
        try:
            if( userCommand[0] not in commandListe):
                raise CommandError
            
            if(userCommand[0] == "ls"):
                ls(getNbArgs(userCommand=userCommand))

            if(userCommand[0] == "pwd"):
                pwd(getNbArgs(userCommand=userCommand))
                
            if(userCommand[0] == "cat"):
                if(len (userCommand) == 2):
                    cat(userCommand[1], getNbArgs(userCommand=userCommand))
                else:
                    raise ArgumentError(1,getNbArgs(userCommand=userCommand))
                                   
        except CommandError as e:
            print("Error: ", e)
            
        except ArgumentError as e:
            print("Error: ", e)
        finally:
            userCommand = getCommandFromUSer()

    print("%")

def getCommandFromUSer():
    userCommand = input("ccsh> ")
    return userCommand.split()

def getNbArgs(userCommand):
    return (len(userCommand) - 1)

if __name__ == "__main__":
    main()