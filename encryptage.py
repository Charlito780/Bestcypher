import math
 
message = int(input("Enter the message to be encrypted: ")) 

#Données RSA : valeurs temporaires 
p = 11
q = 7
e = 3
n = p*q

 #Encryptage
def encryptage(message_encrypt):
    #math.pow renvoie un nombre à une certaine puissance, 
    #c'est-à-dire base^exposant
    #ici message_encrypt=base^exposant[n]
    mc = math.pow(message_encrypt,e) % n
    mc=mc%n
    print("Encrypted Message is: ", mc)
    return mc
 
print("Original Message is: ", message)


#MAIN TEMPORAIRE
c = encryptage(message)