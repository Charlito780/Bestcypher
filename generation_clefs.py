#for linux machine
#sudo apt install python3-pip
# #pip install pycryptodome

#for windows machine
#pip install pycryptodomex --no-binary :all:

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
 
keyPair = RSA.generate(3072)
 
pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))
 
print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))
 
#encryptionf
msg = 'A message for encryption'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(msg.encode('utf-8'))

#encrypted = bytes(encryptor.encrypt(msg), 'utf-8')
print("Encrypted:", binascii.hexlify(encrypted))