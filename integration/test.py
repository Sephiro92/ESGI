# -*- coding: utf-8 -*-

from tkinter import *
from tkinter.filedialog import *

def callback():
    filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
    fichier = open(filename)

    #PARTIE TRAITEMENT###################################################
    traitement = fichier
    contenu = [x.replace("\n", "") for x in traitement.readlines()]

    tabline = "rien"
    line = "rien"

    for n in contenu :
        tabline = n.split()
        tabline.append('vide')
        if tabline[0] == "username" :
            line = n
            line = line.split()

    #print (str(line))
    user = line[1]
    cryptword = line[4]
    rendu = 'username: '+user, 'password: '+cryptword
    traitement.close()

    ###################################################################
    result = open("result.txt", "w")
    result.write(str(rendu))
    result.close()
    ####################################################################
    #content = result.read()
    
    
    fichier.close()

    result = open("result.txt", "r")
    resulta = result.read()
    result.close()



    Label(fenetre, text=resulta).pack(padx=10, pady=10)


# fenètre

fenetre = Tk()

Button(text='Parcourir', command=callback).pack()

fenetre.mainloop()