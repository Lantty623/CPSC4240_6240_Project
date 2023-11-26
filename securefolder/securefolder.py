#!/usr/bin/python3
import hashlib
import sys
import os
import subprocess

# if __name__ == "__main__":
    
    # n = len(sys.argv)
    # if sys.argv[1] == 'create':
    #     if sys.argv[2] != None:
    #         os.mkdir(sys.argv[2])
    #         password = input("Enter The Folder's Password: ")
    #         hashedPassword = hashlib.sha512(password.encode())
    #         with open(sys.argv[2] + "/.password.txt", "w") as f:
    #             f.write(hashedPassword.hexdigest())
    #             f.close()
    #     if sys.argv[2] == None:
    #         folderName = input("Please enter a folder name: ")
    #         os.mkdir(folderName)
    #         password = input("Enter The Folder's Password: ")
    #         hashedPassword = hashlib.sha512(password.encode())
    #         with open(sys.argv[2] + "/.password.txt", "w") as f:
    #             f.write(hashedPassword.hexdigest())
    #             f.close()
    # else:
    #     print("Invalid argument, please use argument \"create\" to create a secure folder")

def create_directory(directory_path):
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
            print(f"Directory '{directory_path}' created.")
        except OSError as e:
            print(f"Error creating directory '{directory_path}': {e}")

n = len(sys.argv)
if (n <= 1):
    folderPath = input("Please enter a folder path: ")
    password = input("Enter The Folder's Password: ")
    create_directory(folderPath)

    hashedPassword = hashlib.sha512(password.encode())
    with open(folderPath + "/.password.txt", "w") as f:
        f.write(hashedPassword.hexdigest())
        f.close()
elif (n == 2):
    folderPath = sys.argv[1]
    password = input("Enter The Folder's Password: ")
    create_directory(folderPath)

    hashedPassword = hashlib.sha512(password.encode())
    with open(folderPath + "/.password.txt", "w") as f:
        f.write(hashedPassword.hexdigest())
        f.close()
elif (n == 3):
    folderPath = sys.argv[1]
    password = sys.argv[2]
    create_directory(folderPath)

    hashedPassword = hashlib.sha512(password.encode())
    with open(folderPath + "/.password.txt", "w") as f:
        f.write(hashedPassword.hexdigest())
        f.close()
else:
    example = "\n\nEXAMPLE:\n\nsecurefolder path/to/folder password"
    subprocess.run(['zenity', '--info', '--title=ERROR..', '--text= ONLY Need 2 Arguments: FolderPath and password' + example])

