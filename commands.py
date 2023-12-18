import os
def ls():
    current_directory = os.getcwd()

    files = os.listdir(current_directory)
    for file in files:
        print(file)
def pwd():
    print(os.getcwd())