# Secure Folder

Uses a CLI through BASH to create a password protected folder using SHA512 (can be changed) to keep password secure in plain site.  

## Setup

- No additional prerequisites

## Installation

- No additional steps

## Design

- Overloads cd, mv, cp, rm, rmdir in the BASH shell to require your password when working with a directory that has a password attached to it 
- Uses SHA512 to secure your password and stores it in your secure folder

## Limitations

- Only compatible with the BASH interface

## Further Development

- Make it cross compatible with all terminals and the native GUI
- Accessible as a shared folder through a network
- Ensure that any command that edits/changes a folder in any way will require a password
- Secure ~/.bashrc file to ensure root access is required to edit

## Code and Components

### addAlias.py

- Adds the function overrides for cd, mv, cp, rm, and rmdir directly to the ~/.bashrc file

### bashfunctionoverwrites.txt

- File that contains the BASH script to be added to ~/.bashrc

### bashRCbackup.txt

- File that holds your original ~/.bashrc script in case of error

### hashtest.py

- Outputs a SHA512 encrypted password based on what was entered on the command line.  
 Can be used separately by entering python3 hashtest.py <password> on the command line.

### Makefile

- Makefile that runs the startscript.sh

### securefolder.py

- Python file that prompts user to create the secured folder.
- **Command-Line Arguments**:
  - `create`: option used to create a secure folder
- Asks for password
- **Further Development**:
  - add option 'add' to change a folder from secure to normal
  - add option 'remove' to change a folder from normal to secure


### startscript.sh

- Script that moves hastest.py and securefolder.py to ~/bin and runs addAlias.py

## Usage

- Run make while securefolder is your current working directory
- Enter 'securefolder create <foldername>' in any directory under your home directory to create a secure folder
