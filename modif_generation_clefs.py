#for linux machine
#pip install pycryptodome
#sudo apt install python3-pip

#for windows machine
#pip install pycryptodomex --no-binary :all:
#--no-use-wheel


 
from fileinput import close
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import ast
import os

def generation_clefs():
    #generation clefs public et privée
    keyPair = RSA.generate(3072)
    pubKey = keyPair.publickey()
    # .exportKey() transforme en PKCK#8 : la syntaxe de clef la plus répendue
    pubKeyPEM = pubKey.exportKey()
    privKeyPEM = keyPair.exportKey()
    creation_fichier(nom_fichier = "pubKey")
    ecrire_alasuite("pubKey", "Public key: (n="+hex(pubKey.n)+" e=" +hex(pubKey.e)+")")
    ecrire_alasuite("pubKey", '\r' + pubKeyPEM.decode('ascii'))

    creation_fichier(nom_fichier = "privKey")
    ecrire_alasuite("privKey", "Private key: (n="+hex(pubKey.n)+" d=" +hex(keyPair.d)+")")
    ecrire_alasuite("privKey", '\r' + privKeyPEM.decode('ascii'))
    return pubKey,keyPair, pubKeyPEM, privKeyPEM

 
#fction encryptage   
def encryptage(pubKey):
    #msg = 'A message for encryption'
    path = os.path.abspath(os.getcwd())
    conc=path+"/msg.txt"
    file=open(conc,'r')
    msg=str(file.readlines())
    file.close
    #fction d'encriptage en elle même
    encryptor = PKCS1_OAEP.new(pubKey)
    encrypted = encryptor.encrypt(msg.encode('utf-8'))
    #Ecriture dans "/Encrypte_str.txt"
    #print("Encrypted:", binascii.hexlify(encrypted))
    conc=path+"/Encrypte_str.txt"
    file=open(conc, "w")
    file.write(str(bytes(encrypted)))
    file.close
    return encrypted

#AH... la fction qui bug
#decryptage enregistré => peut-etre inutil
def decryptage(nomFichier,keyPair,pubKey):
    path = os.path.abspath(os.getcwd())
    conc=path+"/"+nomFichier+".txt"
    file=open(conc,'r')
    encryted=file.readline()
    encrypted=conc.join([l.rstrip for l in file])
    file.close
     #fction de decriptage en elle même
    decryptor = PKCS1_OAEP.new(keyPair)
    decrypted= decryptor.decrypt(ast.literal_eval(str(encrypted)))
    conc=path+"/decryptage.txt"
    #print("creation fich:", conc)
    file=open(conc, "w")
    file.write(str(binascii(encrypted)))
    file.close
    return decrypted

def creation_fichier(nomFichier):
    path = os.path.abspath(os.getcwd())
    conc=path+"/"+nomFichier+".txt"
    file=open(conc,"w")
    file.close
    return

def ecraser(nomFichier, a_ecrire):
    path = os.path.abspath(os.getcwd())
    conc=path+"/"+nomFichier+".txt"
    file=open(conc,"w")
    file.write(a_ecrire)
    file.close
def ecrire_alasuite(nomFichier, a_ecrire):
    path = os.path.abspath(os.getcwd())
    conc=path+"/"+nomFichier+".txt"
    file=open(conc,"a")
    file.write(a_ecrire)
    path = os.path.abspath(os.getcwd())
    conc=path+"/"+nomFichier+".txt"
    file=open(conc, 'a')
    file.write(a_ecrire)
    file.close

#ouvre un fichier d'addresse"File_Name" sinon il faut donner toute l'adresse
#File_object = open (r "File_Name", "Access_Mode")


#MAIN (temporaire)
#=> attention message definit par defaut dans main et nn demandé a utilisateur  (TEMPORAIRE)
def main() :
    #données demandées a utilisiateur (util pour encryption)
    msg = 'A message for encryption'
    ecraser("le message", msg)
    #Appel fonctions
    pubKey,keyPair,pubKeyPEM,privKeyPEM=generation_clefs()
    encrypted = encryptage(pubKey)
    decrypted = decryptage("Encryte_str",keyPair,pubKey)

    #Affichage console (Temporaire) : sera implementé en .txt >> file.read()
     #print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
     #print(pubKeyPEM.decode('ascii'))
     #print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
     #print(privKeyPEM.decode('ascii'))
     #print("Encrypted:", binascii.hexlify(encrypted))
     #print("Decrypted:", str(decrypted))
    
    
main()
