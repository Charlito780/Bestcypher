#for linux machine
#pip install pycryptodome
#sudo apt install python3-pip

#for windows machine
#pip install pycryptodomex --no-binary :all:
#--no-use-wheel


 
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import ast
 
def generation_clefs():
    #generation clefs public et privée
    keyPair = RSA.generate(3072)
    pubKey = keyPair.publickey()
    # .exportKey() transforme en PKCK#8 : la syntaxe de clef la plus répendue
    pubKeyPEM = pubKey.exportKey()
    privKeyPEM = keyPair.exportKey()
    return pubKey,keyPair, pubKeyPEM, privKeyPEM

 
#fction encryptage   
def encryptage(pubKey,msg):
    #msg = 'A message for encryption'
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg.encode('utf-8'))
    
    return encrypted


def decryptage(keyPair,encrypted):
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted= decryptor.decrypt(ast.literal_eval(str(encrypted)))
    return decrypted

#MAIN (temporaire)
#=> attention message definit par defaut dans main et nn demandé a utilisateur  (TEMPORAIRE)
def main() :
    #données demandées a utilisiateur (util pour encryption)
    msg = 'A message for encryption'

    #Appel fonctions
    pubKey,keyPair,pubKeyPEM,privKeyPEM=generation_clefs()
    encrypted = encryptage(pubKey,msg)
    decrypted = decryptage(keyPair,encrypted)

    #Affichage console (Temporaire) : sera implementé en .txt >> file.read()
    print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
    print(pubKeyPEM.decode('ascii'))
    print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
    print(privKeyPEM.decode('ascii'))
    print("Encrypted:", binascii.hexlify(encrypted))
    print("Decrypted:", str(decrypted))
    
    
main()