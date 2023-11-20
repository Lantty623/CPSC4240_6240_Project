#!/usr/bin/python3
import hashlib
import sys
import os

if __name__ == "__main__":
    
    n = len(sys.argv)
    if sys.argv[1] != None:
        hashedPassword = hashlib.sha512(sys.argv[1].encode())
        print(hashedPassword.hexdigest())