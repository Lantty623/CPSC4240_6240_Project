import os
import json
from crypto_utils import CryptoUtils


class FileProcessor:
    def __init__(self, key):
        self.crypto = CryptoUtils(key)

    def process_directory(self, root_dir, target_dir, base_dir='', encrypt=True):

        for root, dirs, files in os.walk(root_dir):
            # Create corresponding structure in target directory
            relative_path = os.path.relpath(root, root_dir)
            target_root_dir = os.path.join(target_dir, relative_path)
            os.makedirs(target_root_dir, exist_ok=True)

            for file in files:
                file_path = os.path.join(root, file)

                if encrypt:
                    # Handle encryption
                    target_file_path = os.path.join(target_root_dir, file + '.enc')
                    self.crypto.encrypt_file(file_path, target_file_path)

                    # Write metadata to a file in the target directory
                    metadata_file_path = target_file_path + '.meta'
                    with open(metadata_file_path, 'w') as f:
                        metadata = {
                            'original_path': file_path
                        }
                        json.dump(metadata, f)

                else:
                    # Skip non-encrypted files during decryption
                    if not file.endswith('.enc'):
                        continue

                    # Handle decryption
                    metadata_file_path = file_path + '.meta'


                    try:
                        with open(metadata_file_path, 'r') as f:
                            metadata = json.load(f)
                            original_path = metadata['original_path']

                            # Reconstruct the full original path for nested directories
                            decrypted_file_path = os.path.join(base_dir, original_path)
                    except (FileNotFoundError, json.JSONDecodeError):
                        continue  # Skip if metadata is missing or corrupted

                    self.crypto.decrypt_file(file_path, decrypted_file_path)

    def process_path(self, path, base_encrypt_folder, base_decrypt_folder, encrypt):
        """
        Encrypts or decrypts a file or all files in a directory and saves them in specified folders.

        :param key: Encryption key.
        :param path: Path to the file or directory.
        :param base_encrypt_folder: Folder to save encrypted files.
        :param base_decrypt_folder: Folder to save decrypted files.
        :param encrypt: True for encryption, False for decryption.
        """

        # Check if the source path exists
        if not os.path.exists(path):
            print(f"Error: The specified path '{path}' does not exist.")
            return

        if os.path.isfile(path):

            # Adjust the metadata file path based on whether we are encrypting or decrypting
            if encrypt:
                metadata_file_path = os.path.join(base_encrypt_folder, os.path.basename(path) + '.meta')
            else:
                # Remove '.enc' from the file name for decryption
                metadata_file_path = path.replace('.enc', '') + '.meta'

            if encrypt:
                # Define the encrypted file path
                encrypted_file_path = os.path.join(base_encrypt_folder, os.path.basename(path) + '.enc')
                self.crypto.encrypt_file(path, encrypted_file_path)
                # Optionally remove the original file
                # os.remove(path)

                # Write metadata to a separate file
                with open(metadata_file_path, 'w') as f:
                    json.dump({'original_path': path}, f)
            else:
                # Extract metadata from the encrypted file
                # Read metadata from the separate file
                with open(metadata_file_path, 'r') as f:
                    metadata = json.load(f)
                    original_path = metadata['original_path']
                    decrypted_file_path = os.path.join(base_decrypt_folder, os.path.basename(original_path))

                self.crypto.decrypt_file(path, decrypted_file_path)
                # Optionally remove the encrypted file
                # os.remove(path)

        elif os.path.isdir(path):
            if encrypt:
                target_dir = os.path.join(base_encrypt_folder, os.path.basename(path))
            else:
                target_dir = os.path.join(base_decrypt_folder, os.path.basename(path))
            self.process_directory(path, target_dir, base_decrypt_folder, encrypt)
