# File Encryption and Decryption Tool

This tool is designed for the encryption and decryption of files and directories, implementing AES encryption in CFB mode. It offers a command-line interface, suitable for a variety of use cases including securing sensitive data.

## Features

- **Encryption & Decryption**: Supports both encryption and decryption of files and directories.
- **AES Encryption**: Utilizes AES encryption in CFB mode for robust security.
- **Command-Line Interface**: Easy to use in scripts and automation tasks.
- **Key Management**: Securely generates and stores encryption keys.

## Setup

### Prerequisites

- Python 3.x
- Cryptography library
- Python-dotenv package

### Installation

1. Clone the repository or download the source code.
2. Install the required Python packages:
   ```bash
   pip install cryptography python-dotenv
   
## Design and Architecture

The design of the File Encryption and Decryption Tool is modular, focusing on separation of concerns, which allows for easier maintenance and potential scalability. Here's an overview of its design:

### Modular Design

- **Key Management (`KeyManager`)**: This module is solely responsible for managing the encryption key. It isolates key generation, storage, and retrieval functionalities, ensuring that key management is independent of the core encryption/decryption logic.

- **Encryption/Decryption Operations (`CryptoUtils`)**: This module handles the core cryptographic operations. It abstracts the complexity of the cryptographic processes, providing simple methods for encrypting and decrypting files. This separation allows for the cryptographic logic to be updated or changed without affecting other parts of the application.

- **File Processing (`FileProcessor`)**: Responsible for processing files and directories, this module connects the cryptographic operations with the filesystem. It determines whether a path is a file or a directory and applies the appropriate encryption or decryption operation. This module is crucial for handling batch operations on directories.

### Scalability and Maintenance

- The tool's modular architecture allows for easy updates and maintenance. For example, if a new encryption algorithm is to be implemented, changes would primarily be made in the `CryptoUtils` module without affecting key management or file processing logic.
- The separation of concerns also means that new features, such as adding support for different file types or integrating additional security measures, can be done with minimal impact on existing functionalities.

### Command-Line Interface

- The `main.py` script serves as the command-line interface (CLI), making the tool scriptable and easy to integrate into various workflows.
- The CLI uses `argparse` to handle user inputs, providing a user-friendly way to specify the mode of operation (encryption or decryption), the file or directory to process, and the target base folder.

### Security Considerations

- The encryption key is securely generated and stored, ensuring that encrypted files can only be decrypted with the correct key.
- The tool does not automatically create directories if they do not exist, reducing the risk of misplacing sensitive files.

## Conclusion

The File Encryption and Decryption Tool's design is centered around robust security practices, ease of use, and maintainability. Its modular structure ensures that each component can be independently developed, maintained, and scaled.

## Getting Started

To begin using the tool, refer to the [Usage](#usage) section above.

## Code Structure and Components

The tool consists of several Python classes, each responsible for a specific aspect of the encryption and decryption process. Below is an overview of these classes and their functions:

### `KeyManager` Class

- **Purpose**: Manages the encryption key.
- **Functions**:
  - `generate_and_store_key()`: Generates a new encryption key and stores it in a `.env` file. This is only done if a key does not already exist.
  - `load_key_from_env()`: Loads the encryption key from the `.env` file.
  - `key_exists()`: Checks if the encryption key already exists in the environment.

### `CryptoUtils` Class

- **Purpose**: Handles the actual encryption and decryption operations.
- **Functions**:
  - `encrypt_file(input_file_path, output_file_path)`: Encrypts a file. It uses the AES algorithm in CFB mode and writes the encrypted data to the specified output file.
  - `decrypt_file(input_file_path, output_file_path)`: Decrypts a file. Reads the encrypted data and IV, performs decryption, and writes the decrypted data to the specified output file.

### `FileProcessor` Class

- **Purpose**: Manages file and directory processing for encryption and decryption.
- **Functions**:
  - `process_directory(root_dir, target_dir, base_dir, encrypt)`: Processes all files in a directory, encrypting or decrypting them as specified. It recursively handles subdirectories.
  - `process_path(path, base_encrypt_folder, base_decrypt_folder, encrypt)`: Determines whether the given path is a file or a directory and processes it accordingly. It also handles the creation of metadata files during encryption.

### Main Script (`main.py`)

- **Functionality**: Serves as the entry point for the tool. It parses command-line arguments and initiates the encryption or decryption process based on user input.
- **Command-Line Arguments**:
  - `-e/--encrypt`: Flag to specify encryption mode.
  - `-d/--decrypt`: Flag to specify decryption mode.
  - `path`: Path to the file or directory to process.
  - `base_folder`: Base folder for storing encrypted/decrypted files.

## Getting Started

To begin using the tool, simply run the `main.py` script with the appropriate command-line arguments, as detailed in the Usage section above.

For example, to encrypt a directory named `my_folder` and store the encrypted files in the `Encrypted` directory, use:
```bash
python main.py -e my_folder Encrypted
```

## Key Generation and Environment Setup

The tool will automatically generate an encryption key the first time it's run. This key is stored in a `.env` file in the same directory as the script. Make sure not to lose this key. Without it, encrypted files cannot be decrypted.

## Usage

### Encrypting/Decrypting a File or Directory

To encrypt/decrypt a file or directory, use the following command:
```bash
   python main.py -e <path_to_file_or_directory> <target_base_folder>
```
**-e/-d**: Flag to specify encryption/decryption mode.
**<path_to_encrypted_file_or_directory>**: Path to the file or directory you want to decrypt.
**<target_base_folder>**: Folder where decrypted files will be stored.

## Notes

- Ensure that the `.env` file with the encryption key is kept secure. The encryption key stored in this file is crucial for both encrypting and decrypting your files.
- The tool checks if the specified target base folder exists and will not create it if it does not. Please make sure that your specified target folder for storing encrypted or decrypted files already exists.
- For security, the tool does not automatically create non-existent directories. This measure prevents unintentional directory creation that might lead to security vulnerabilities or organizational issues.

# Secure Folder

Uses a CLI through BASH to create a password protected folder using SHA512 (can be changed) to keep password secure in plain site.  

## Setup

-- No additional prerequisites

## Installation

-- No additional steps

## Design

-- Overloads cd, mv, cp, rm, rmdir in the BASH shell to require your password when working with a directory that has a password attached to it 
-- Uses SHA512 to secure your password and stores it in your secure folder

## Limitations

-- Only compatible with the BASH interface

## Further Development

-- Make it cross compatible with all terminals and the native GUI
-- Accessible as a shared folder through a network

## Code and Components

### addAlias.py

Adds the function overrides for cd, mv, cp, rm, and rmdir directly to the ~/.bashrc file

### bashfunctionoverwrites.txt

-- File that contains the BASH script to be added to ~/.bashrc

### bashRCbackup.txt

-- File that holds your original ~/.bashrc script in case of error

### hashtest.py

-- Outputs a SHA512 encrypted password based on what was entered on the command line.  
-- Can be used separately by entering python3 hashtest.py <password> on the command line.

### Makefile

-- Makefile that runs the startscript.sh

### securefolder.py

-- Python file that prompts user to create the secured folder.
- **Command-Line Arguments**:
  - `create`: option used to create a secure folder
-- Asks for password
- **Further Development**:
  - add option 'add' to change a folder from secure to normal
  - add option 'remove' to change a folder from normal to secure


### startscript.sh

-- Script that moves hastest.py and securefolder.py to ~/bin and runs addAlias.py

## Usage

-- Run make while securefolder is your current working directory
-- Enter securefolder create <foldername> in any directory under your home directory to create a secure folder




