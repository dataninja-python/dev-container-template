# app/security.py
"""Module for handling security aspects of containers using Podman."""

import subprocess
import os
from cryptography.fernet import Fernet

class SecurityManager:
    def __init__(self, key_file='secret.key'):
        self.key_file = key_file
        self.key = self.load_or_generate_key()

    def load_or_generate_key(self):
        """
        Load an encryption key from a file, or generate a new one.
        
        :return: A key for encryption/decryption.
        """
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as file:
                key = file.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as file:
                file.write(key)
        return key

    def encrypt_data(self, data):
        """
        Encrypt data.
        
        :param data: Data to be encrypted.
        :return: Encrypted data.
        """
        f = Fernet(self.key)
        encrypted_data = f.encrypt(data.encode('utf-8'))
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        """
        Decrypt data.
        
        :param encrypted_data: Data to be decrypted.
        :return: Decrypted data as a string.
        """
        f = Fernet(self.key)
        decrypted_data = f.decrypt(encrypted_data).decode('utf-8')
        return decrypted_data

    def generate_ssh_key(self, ssh_key_path='~/.ssh/id_rsa'):
        """
        Generate an SSH key pair.
        
        :param ssh_key_path: The file path to store the SSH key.
        """
        ssh_key_path = os.path.expanduser(ssh_key_path)
        if not os.path.exists(ssh_key_path):
            try:
                subprocess.run(
                    ["ssh-keygen", "-t", "rsa", "-b", "4096", "-N", "", "-f", ssh_key_path],
                    check=True,
                    text=True
                )
                print(f"SSH key generated at {ssh_key_path}.")
            except subprocess.CalledProcessError as e:
                print(f"Failed to generate SSH key: {e.stderr}")
        else:
            print("SSH key already exists.")

# Example usage:
if __name__ == "__main__":
    security = SecurityManager()

    # Encrypt and decrypt data
    secret_data = "secret_password"
    encrypted = security.encrypt_data(secret_data)
    print(f"Encrypted: {encrypted}")
    decrypted = security.decrypt_data(encrypted)
    print(f"Decrypted: {decrypted}")

    # Generate SSH key
    security.generate_ssh_key()

