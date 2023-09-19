#Damian Lefebvre
#31 aout 2023
#TP2

#import
import random

#definir le jeu pour l'activer apres
def jeu_de_devinettes():
    #le nombre de possibilite que il peut avoir
    borne_minimale = 0
    borne_maximale = 1000
    #random le nombre
    nombre_choisi = random.randint(borne_minimale, borne_maximale)
    #definir le nombre d'essais
    nb_essais = 0

    #mise en contexte
    print("Point de départ :")
    print(f"J'ai choisi un nombre au hasard entre {borne_minimale} et {borne_maximale}.")
    print("À vous de le deviner...")

    #pour que ca soit possible de recommencer le jeu infini de fois
    while True:
        #demande pour le premier essai
        essai = int(input("Entrez votre essai : "))
        #ajouter 1 essai a notre compte
        nb_essais += 1

        #pour  dire si le nombre est plus haut ou bas
        if essai < nombre_choisi:
            print(f"Mauvais choix, le nombre est plus grand que {essai}")
        elif essai > nombre_choisi:
            print(f"Mauvaise réponse, le nombre est plus petit que {essai}")
        else:
            #si on a eu bon
            print("Bravo! Bonne réponse")
            #nombre d'essai pour savoir le nombre
            print(f"Vous avez réussi en : {nb_essais} essai(s).")
            #demande pour une nouvelle partie
            nouvelle_partie = input("Voulez-vous faire une autre partie (o/n)? ")
            #commence la nouvelle partie 
            if nouvelle_partie.lower() == "o":
                #appel a notre jeu
                jeu_de_devinettes()
            else:
                #arret du jeu
                print("Merci et au revoir...")
                break

# Démarrer le jeu
jeu_de_devinettes()
