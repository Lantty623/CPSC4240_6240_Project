#!/usr/bin/python3
import hashlib
import sys
import os

if __name__ == "__main__":
    
    n = len(sys.argv)
    if sys.argv[1] == 'create':
        if sys.argv[2] != None:
            os.mkdir(sys.argv[2])
            password = input("Enter The Folder's Password: ")
            hashedPassword = hashlib.sha512(password.encode())
            with open(sys.argv[2] + "/.password.txt", "w") as f:
                f.write(hashedPassword.hexdigest())
                f.close()
        if sys.argv[2] == None:
            folderName = input("Please enter a folder name: ")
            os.mkdir(folderName)
            password = input("Enter The Folder's Password: ")
            hashedPassword = hashlib.sha512(password.encode())
            with open(sys.argv[2] + "/.password.txt", "w") as f:
                f.write(hashedPassword.hexdigest())
                f.close()
    else:
        print("Invalid argument, please use argument \"create\" to create a secure folder")