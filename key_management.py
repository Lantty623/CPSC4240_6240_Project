import os

class KeyManager:
    def __init__(self, env_file='.env'):
        self.env_file = env_file

    def generate_and_store_key(self):
        # Check if the key already exists
        if not self.key_exists():
            key = os.urandom(32)  # 32 bytes * 8 = 256 bits
            hex_key = key.hex()

            # Write the hex key to a .env file
            with open(self.env_file, 'w') as file:
                file.write(f"ENCRYPTION_KEY={hex_key}\n")

            return key
        else:
            raise Exception("Encryption key already exists. Not generating a new one.")

    def load_key_from_env(self):
        hex_key = os.getenv('ENCRYPTION_KEY')
        if hex_key is None:
            raise ValueError("Encryption key not found in environment variables")
        return bytes.fromhex(hex_key)

    def key_exists(self):
        key = os.getenv('ENCRYPTION_KEY')
        return key is not None and len(key) >= 16  # Checking for minimum length in hex (8 bytes = 16 hex characters)

    # Add other key management methods as needed
