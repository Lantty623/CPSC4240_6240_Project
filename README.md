# Secure Folder and Encryption/Decryption

## Installation

- install python3 and pip
- pip install cryptography python-dotenv
- (if required) sudo apt install zenity

## Code Setup
- Download from github or if you have the zip then unzip the contents
- Go into that folder and open the command prompt.
- First, run "make" and wait for successful message: " everything is setup and good to go! "
- Second, run "make gui" and wait for successful message: " gui is setup and ready to go! " 


## Design

- Overloads cd, mv, cp, rm, rmdir in the BASH shell to require your password when working with a directory that has a password attached to it 
- Uses SHA512 to secure your password and stores it in your secure folder

## Limitations

- Linux: Ubuntu GNOME GUI → Nautilus
- python3

## Further Development

- Make it cross compatible with all terminals and the native GUI
- Accessible as a shared folder through a network
- Ensure that any command that edits/changes a folder in any way will require a password
- Secure ~/.bashrc file to ensure root access is required to edit

## Usage

- Use the file manager and right-click menu -> scripts.
- Could also run those scripts through command prompt
  - run "FolderSecure" (use this to put a password lock on a folder)
  - run "FolderSecure_Encrypt" (use this to put a password lock on a folder and also encrypt the folder)
  - run "FolderUnlock" (use this to remove the password lock on a folder)
  - run "FolderUnlock_Decrypt" (use this to remove the password lock on a folder and also decrypt the folder)
  - run "Encrypt" (use this to encrypt a folder)
  - run "Decrypt" (use this to decrypt a folder)

- Or directly run code using the command prompts as shown below:
  - securefolder
    - takes in 0 to 2 arguements to run the script (arguments: /path/to/folder and password)
    - for example: just run "securefolder" or "securefolder /path/to/folder password"
  - For running encryptions/decryptions
    - go to the folder that has downloaded code and go to Crypto folder
    - run "Python3 main.py" with arguments:
      - " -e" for encryption or " -d" for decryption
      - "path/to/folder/to/encrypt" or path-to-decrypt
      - "destination/folder/path"

