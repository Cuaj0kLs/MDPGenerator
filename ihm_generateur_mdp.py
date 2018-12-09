#!/usr/bin/python
#coding:utf-8
                                        ###################################################
                                        #########   Générateur de mot de passe,   #########
                                        #########  Aléatoire simple et efficace   #########
                                        #########           By Breizhux           #########
                                        #########       xavier.lanne@gmx.fr       #########
                                        ###################################################


from Tkinter import *
from random import *
import pyperclip


# Définition des types de chaine à utiliser pour le mot de passe :
numerique = "0123456789"
alphanumerique = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
alphanumerique_et_speciaux = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,:;!?-_&=+#@$%"


def creation_mot_passe():

    # Récupération des valeurs choisis :
    chaine = choix_chaine.get()

    # Préviens si aucun type de chaine n'a été séléctionné !
    if chaine == "" :
        champ_texte.delete(0.0, END)
        champ_texte.insert(END, "\n Veuillez choisir le type de chaine que vous voulez utiliser !")

    longueur = int(longueur_mot_passe.get())


    # Définition de la liste qui va contenir le mot de passe aléatoire :
    M = []

    # On choisi aléatoirement les caractères
    for i in range(longueur) :
        M.append(choice(chaine))

    # On converti la liste en chaine de caractères
    mdp = "".join(M)

    # On la copie dans le presse-papier
    pyperclip.copy(mdp)


    # Définition du message de fin :
    if longueur <= 90 :
        texte = "\n *** Votre mot de passe est : " + mdp + "\n\n Ce mot de passe a été copié dans le presse-papier."
    else :
        texte = " *** Votre mot de passe est : " + mdp + "\n Ce mot de passe a été copié dans le presse-papier."
    # Affichage de fin de la génération !
    champ_texte.delete(0.0, END)
    champ_texte.insert(END, texte)





                                                                    ###########
                                                                    ### IHM ###
                                                                    ###########

# Définition des propriétés de la fenetre :
fenetre = Tk()
fenetre.title("Générateur de mot de passe aléatoire")
fenetre.geometry("800x470")


# Zone de l'explication du programme :
champ_nom = Label(fenetre, text = "Bienvenus dans le générateur de mot de passe aléatoire !!")
champ_nom.grid(row=1, column=3, padx=230, pady=19)


# Zone de demande de choisir un type de caractère !
champ_entre_hash = Label(fenetre, text = "Choisissez le type de caractère que vous voulez :")
champ_entre_hash.grid(row=2, column=3, pady=9)

# Boutton-radio pour choisir le type de mot de passe :
choix_chaine = StringVar()

choix_numerique = Radiobutton(fenetre, text = "numerique", variable = choix_chaine, value=numerique)
choix_alphanumerique = Radiobutton(fenetre, text = "alphanumerique", variable = choix_chaine, value=alphanumerique)
choix_alphanumerique_et_speciaux = Radiobutton(fenetre, text = "alphanumerique et speciaux", variable = choix_chaine, value=alphanumerique_et_speciaux)

choix_numerique.grid(row=3, column=3)
choix_alphanumerique.grid(row=4, column=3)
choix_alphanumerique_et_speciaux.grid(row=5, column=3)


# Zone de demande de choisir un type de caractère !
champ_entre_hash = Label(fenetre, text = "\nChoisissez la longueur du mot de passe :")
champ_entre_hash.grid(row=6, column=3, pady=9)

# Zone de spinbox, pour choisir la longueur du mot de passe :
longueur_mot_passe = Spinbox(fenetre, from_=9, to=360)
longueur_mot_passe.grid(row=7, column=3, pady=9)
#longueur_mot_passe.insert("19")


# Zone d'affichage :
champ_texte = Text(fenetre, height=6, width=90, wrap=WORD)
champ_texte.grid(row=8, column=3, pady=19)
champ_texte.insert(END, "\n Générer un mot de passe !!")


# Affichage du bouton Générer :
bouton_generer = Button(fenetre, text="Générer", command=creation_mot_passe)
bouton_generer.grid(row=9, column=3, pady=9)


# Affichage d'un bouton Quitter :
bouton_quitter = Button(fenetre, text="Quitter", command=fenetre.destroy)
bouton_quitter.grid(row=10, column=3, pady=19)


fenetre.mainloop()
