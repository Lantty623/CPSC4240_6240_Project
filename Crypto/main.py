import sys, os
from dotenv import load_dotenv
import argparse
from key_management import KeyManager
from file_processor import FileProcessor

def main():
    load_dotenv()

    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Encrypt or decrypt files and directories.")
    parser.add_argument("path", help="Path to the file or directory to process")
    #parser.add_argument("base_folder", help="Base folder for encrypted/decrypted files")
    parser.add_argument("base_folder", nargs='?', default=os.getcwd(),
                        help="Base folder for encrypted/decrypted files (defaults to current directory if not provided)")

    # Set up mutually exclusive group for -e/--encrypt and -d/--decrypt
    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument("-e", "--encrypt", help="Encrypt the specified file or directory", action="store_true")
    mode_group.add_argument("-d", "--decrypt", help="Decrypt the specified file or directory", action="store_true")

    args = parser.parse_args()

    # Standardize the path format by removing any trailing slash
    path = args.path.rstrip("/")
    base_folder = args.base_folder.rstrip("/")

    # Check if the target_base_folder exists
    if not os.path.exists(base_folder):
        print(f"Error: The target base folder '{base_folder}' does not exist.")
        sys.exit(1)

    key_manager = KeyManager()
    try:
        # Generate and store the key only if it doesn't already exist
        if not key_manager.key_exists():
            key = key_manager.generate_and_store_key()
        else:
            key = key_manager.load_key_from_env()

        processor = FileProcessor(key)

        if args.encrypt:
            processor.process_path(path, base_encrypt_folder=base_folder, base_decrypt_folder=base_folder, encrypt=True)
        elif args.decrypt:
            processor.process_path(path, base_encrypt_folder=base_folder, base_decrypt_folder=base_folder, encrypt=False)
        else:
            print("Invalid mode. Use 'encrypt' or 'decrypt'.")
            sys.exit(1)

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
