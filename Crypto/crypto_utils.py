from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

class CryptoUtils:
    def __init__(self, key):
        self.key = key

    def encrypt_file(self, input_file_path, output_file_path):
        try:
            iv = os.urandom(16)  # AES block size is 16 bytes
            cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=default_backend())
            encryptor = cipher.encryptor()

            with open(input_file_path, 'rb') as infile:
                with open(output_file_path, 'wb') as outfile:
                    outfile.write(iv)  # Write the IV to the output file
                    while True:
                        data = infile.read(1024)
                        if not data:
                            break
                        encrypted_data = encryptor.update(data)
                        outfile.write(encrypted_data)
                    outfile.write(encryptor.finalize())
        except Exception as e:
            print(f"An error occurred during file encryption: {e}")

    # Decrypt a file
    def decrypt_file(self, input_file_path, output_file_path):
        try:
            with open(input_file_path, 'rb') as infile:
                iv = infile.read(16)  # Read the IV from the input file
                cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=default_backend())
                decryptor = cipher.decryptor()

                with open(output_file_path, 'wb') as outfile:
                    while True:
                        data = infile.read(1024)
                        if not data:
                            break
                        decrypted_data = decryptor.update(data)
                        outfile.write(decrypted_data)
                    outfile.write(decryptor.finalize())
        except Exception as e:
            print(f"An error occurred during file decryption: {e}")

