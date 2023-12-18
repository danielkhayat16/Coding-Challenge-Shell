from commands import *
from exception import CommandError

def main():
    print('% cssh')
    commandListe = ["ls", "pwd"]
    userCommand = getCommandFromUSer()
    while(userCommand != "exit"):
        try:
            if( userCommand not in commandListe):
                raise CommandError
            if(userCommand == "ls"):
                ls()
            if(userCommand == "pwd"):
                pwd()
            userCommand = getCommandFromUSer()
                                   
        except CommandError as e:
            print("Error: ", e)
            userCommand = getCommandFromUSer()
    print("%")

def getCommandFromUSer():
    userCommand = input("ccsh> ")
    return userCommand

if __name__ == "__main__":
    main()