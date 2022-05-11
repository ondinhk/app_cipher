from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

# Public
keyPair = RSA.generate(2048)
pubKey = keyPair.publickey()
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM)
print(pubKeyPEM.decode('ascii'))


# Private
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

# Input
msg = bytes(str(input("Enter plain text: ")), 'utf-8')
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))



decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted.decode('utf-8'))
