from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

PATH = '/home/onkhang/PycharmProjects/ATBMTT/Key/'


# Public
def createKey():
    keyPair = RSA.generate(2048)
    pubKey = keyPair.publickey()
    pubKeyPEM = pubKey.exportKey().decode('ascii')
    export_file("publicKey", pubKeyPEM)
    # Private
    privKeyPEM = keyPair.exportKey().decode('ascii')
    export_file("privateKey", privKeyPEM)


def export_file(name, data):
    name = PATH + name + ".pem"
    with open(name, 'w') as f:
        f.write(data)


def en_code(text, pathPublicKey):
    # convert string to byte
    text = bytes(str(text), 'utf-8')
    #
    key = RSA.importKey(open(pathPublicKey).read())
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(text)
    return ciphertext


def de_code(text, pathprivateKey):
    # text = bytes(text,'utf-8')
    key = RSA.importKey(open(pathprivateKey).read())
    cipher = PKCS1_OAEP.new(key)
    message = cipher.decrypt(text)
    return message


if __name__ == '__main__':
    # Define
    pathPub = "../Key/publicKey.pem"
    pathPri = "../Key/privateKey.pem"
