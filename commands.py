import os
from exception import *

def ls(argsNumber):
    if(argsNumber != 0):
        raise ArgumentError(0,argsNumber)
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    for file in files:
        print(file)

def pwd(argsNumber):
    if(argsNumber != 0):
        raise ArgumentError(0,argsNumber)
    print(os.getcwd())

def cat(filePath, argsNumber):
    if(argsNumber != 1):
        raise ArgumentError(0, argsNumber)
    try:
        with open(filePath, 'r') as file:
            file_contents = file.read()
            print(file_contents)
    except FileNotFoundError as e:
        print(e)
