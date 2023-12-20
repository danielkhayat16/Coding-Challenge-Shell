import os
from exception import *
import subprocess


def ls(argsNumber):
    if argsNumber != 0:
        raise ArgumentError(0, argsNumber)
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    for file in files:
        print(file)


def pwd(argsNumber):
    if argsNumber != 0:
        raise ArgumentError(0, argsNumber)
    print(os.getcwd())
    return os.getcwd()


def cat(filePath, argsNumber):
    if argsNumber != 1:
        raise ArgumentError(0, argsNumber)
    try:
        with open(filePath, "r") as file:
            file_contents = file.read()
            print(file_contents)
    except FileNotFoundError as e:
        print(e)


def cd(filePath, argsNumber):
    newDir = os.getcwd()
    if argsNumber != 1:
        raise ArgumentError(1, argsNumber)
    if filePath == "..":
        strToRemove = len(newDir.split("/")[-1])
        newDir = newDir[:-strToRemove]
    else:
        newDir += "/" + filePath
    os.chdir(newDir)


def curl(url, argument, fileName, argsNumber):
    if argsNumber != 3:
        raise ArgumentError(3, argsNumber)
    result = subprocess.run(
        "curl " + url + " " + argument + " " + fileName,
        shell=True,
        capture_output=True,
        text=True,
    )
    print(result.stdout)


def execute_command_pipeline(command, input_text=None):
    try:
        if input_text:
            process = subprocess.Popen(
                command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True
            )
            return process.communicate(input=input_text)[0]
        else:
            process = subprocess.Popen(command, stdout=subprocess.PIPE, text=True)
            return process.communicate()[0]
    except FileNotFoundError as e:
        print(e)


def run_pipeline(commands):
    commands = commands.split("|")
    input_text = None

    for cmd in commands:
        cmd = cmd.split()
        input_text = execute_command_pipeline(cmd, input_text)

    return input_text


def execute_single_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(result.stdout.split()[0])

    except FileNotFoundError as e:
        print(e)
