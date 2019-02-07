# coding: utf-8

import random   
import string
from scipy import *

#crypt = raw_input("votre message : ") 


n = 0
rdm = 0                 
encrypt = [] 
rdm1 = random.randint(0, 4)
rdm2 = random.randint(0, 4)
alpha = list(string.ascii_lowercase)
tab = [['0', '0', '0', '0', '0'],
       ['0', '0', '0', '0', '0'],
       ['0', '0', '0', '0', '0'],
       ['0', '0', '0', '0', '0'],
       ['0', '0', '0', '0', '0']]

while n != 25 :

    
    rdm1 = random.randint(0, 5)
    rdm2 = random.randint(0, 5)
    
    if tab[rdm1][rdm2] == '0' :
        tab[rdm1][rdm2] = alpha[n]
        if alpha[n] == 'u' :
            tab[rdm1][rdm2] = 'z'
        n = n + 1
 #       
    


print(tab)

n = 0

#départ
crypt = raw_input("votre message : ")

while n < len(crypt) :

    if crypt[n] == "a" :
        encrypt.append(tab[0][0])

    if crypt[n] == "b" :
        encrypt.append(tab[0][1])

    if crypt[n] == "c" :
        encrypt.append(tab[0][2])

    if crypt[n] == "d" :
        encrypt.append(tab[0][3])

    if crypt[n] == "e" :
        encrypt.append(tab[0][4])

    if crypt[n] == "f" :
        encrypt.append(tab[1][0])

    if crypt[n] == "g" :
        encrypt.append(tab[1][1])

    if crypt[n] == "h" :
        encrypt.append(tab[1][2])

    if crypt[n] == "i" :
        encrypt.append(tab[1][3])

    if crypt[n] == "j" :
        encrypt.append(tab[1][4])

    if crypt[n] == "k" :
        encrypt.append(tab[2][0])

    if crypt[n] == "l" :
        encrypt.append(tab[2][1])

    if crypt[n] == "m" :
        encrypt.append(tab[2][2])

    if crypt[n] == "n" :
        encrypt.append(tab[2][3])

    if crypt[n] == "o" :
        encrypt.append(tab[2][4])

    if crypt[n] == "p" :
        encrypt.append(tab[3][0])

    if crypt[n] == "q" :
        encrypt.append(tab[3][1])

    if crypt[n] == "r" :
        encrypt.append(tab[3][2])

    if crypt[n] == "s" :
        encrypt.append(tab[3][3])

    if crypt[n] == "t" :
        encrypt.append(tab[3][4])

    if crypt[n] == "u" :
        encrypt.append(tab[4][0])

    if crypt[n] == "v" :
        encrypt.append(tab[4][0])

    if crypt[n] == "w" :
        encrypt.append(tab[4][1])

    if crypt[n] == "x" :
        encrypt.append(tab[4][2])

    if crypt[n] == "y" :
        encrypt.append(tab[4][3])

    if crypt[n] == "z" :
        encrypt.append(tab[4][4])


    n = n + 1

#print(encrypt)

for lettre in encrypt:
     print(lettre),
