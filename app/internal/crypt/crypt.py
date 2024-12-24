from abc import ABC, abstractmethod
from dataclasses import dataclass

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# generate
# password = os.getenv("ENCRYPT_PASSWORD")
# if password is None:
#     raise ValueError("no password")

# salt = os.getenv("ENCRYPT_SALT")
# if salt is None:
#     raise ValueError("no salt")

@dataclass
class EncryptResult:
    result: bytes
    tag: bytes

@dataclass
class DecryptResult:
    result: bytes

class Crypt(ABC):
    @abstractmethod
    def encrypt(self, nonce: str, plain_text: str) -> EncryptResult:
        pass

    def decrypt(self, nonce: str, tag: str, cipher_text: str) -> bytes:
        pass


class CryptImpl:
    def __init__(self, password: str, salt: str):
        self.password = password
        self.salt = salt
        self.key = self.__create_key()

    def __create_key(self) -> bytes:
        byte_password = self.password.encode()
        byte_salt = self.salt.encode()
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=byte_salt,
            iterations=1000000,
        )

        return kdf.derive(byte_password)

    def encrypt(self, nonce: str, plain_text: str) -> EncryptResult:
        byte_nonce = nonce.encode()
        byte_plain_text = plain_text.encode()

        cipher = Cipher(algorithm=algorithms.AES(self.key), mode=modes.GCM(byte_nonce))
        encryptor = cipher.encryptor()

        cipher_text = encryptor.update(byte_plain_text) + encryptor.finalize()

        return EncryptResult(result=cipher_text, tag=encryptor.tag)

    def decrypt(self, nonce: str, tag: str, cipher_text: str) -> bytes:
        cipher = Cipher(algorithm=algorithms.AES(self.key), mode=modes.GCM(initialization_vector=nonce.encode(), tag=tag.encode()))
        decryptor = cipher.decryptor()
        result = decryptor.update(cipher_text.encode()) + decryptor.finalize()

        return result
