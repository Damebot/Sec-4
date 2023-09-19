#Damian Lefebvre
#31 aout 2023
#TP2

import random

#definir le jeu pour l'activer apres
def jeu_de_devinettes():
    borne_minimale = 0
    borne_maximale = 1000
    nombre_choisi = random.randint(borne_minimale, borne_maximale)
    nb_essais = 0

    print("Point de départ :")
    print(f"J'ai choisi un nombre au hasard entre {borne_minimale} et {borne_maximale}.")
    print("À vous de le deviner...")

    #pour que ca soit possible de recommencer le jeu infini de fois
    while True:
        essai = int(input("Entrez votre essai : "))
        nb_essais += 1

        if essai < nombre_choisi:
            print(f"Mauvais choix, le nombre est plus grand que {essai}")
        elif essai > nombre_choisi:
            print(f"Mauvaise réponse, le nombre est plus petit que {essai}")
        else:
            print("Bravo! Bonne réponse")
            print(f"Vous avez réussi en : {nb_essais} essai(s).")
            nouvelle_partie = input("Voulez-vous faire une autre partie (o/n)? ")
            if nouvelle_partie.lower() == "o":
                jeu_de_devinettes()
            else:
                print("Merci et au revoir...")
                break

# Démarrer le jeu
jeu_de_devinettes()
