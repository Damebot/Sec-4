#Damian Lefebvre
#31 aout 2023
#TP3

import random

def jouer():
    niveau_vie = 20
    nombre_victoires = 0
    nombre_defaites = 0
    nombre_victoires_consecutives = 0
    
    while niveau_vie > 0:
        force_adversaire = random.randint(1, 5)
        print("\nPoint de départ :")
        print(f"Vous tombez face à face avec un adversaire de difficulté : {force_adversaire}")
        
        print("Que voulez-vous faire ?")
        print("1- Combattre cet adversaire")
        print("2- Contourner cet adversaire et aller ouvrir une autre porte")
        print("3- Afficher les règles du jeu")
        print("4- Quitter la partie")
        
        choix = input("Entrez votre choix : ")
        
        if choix == "1":
            score_de = random.randint(1, 6)
            print("\nLancer du dé :", score_de)
            
            if score_de > force_adversaire:
                print("Victoire !")
                niveau_vie += force_adversaire
                nombre_victoires += 1
                nombre_victoires_consecutives += 1
                print("Niveau de vie :", niveau_vie)
                print("Nombre de victoires consécutives :", nombre_victoires_consecutives)
            else:
                print("Défaite...")
                niveau_vie -= force_adversaire
                nombre_defaites += 1
                nombre_victoires_consecutives = 0
                print("Niveau de vie :", niveau_vie)
        
        elif choix == "2":
            niveau_vie -= 1
            print("Vous contournez l'adversaire. Pénalité de 1 point de vie.")
            print("Niveau de vie :", niveau_vie)
        
        elif choix == "3":
            print("\nPour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l'adversaire.")
            print("Dans ce cas, le niveau de vie de l'usager est augmenté de la force de l'adversaire.")
            print("Une défaite a lieu lorsque la valeur du dé lancé par l'usager est inférieure ou égale à la force de l'adversaire.")
            print("Dans ce cas, le niveau de vie de l'usager est diminué de la force de l'adversaire.")
        
        elif choix == "4":
            print("\nMerci et au revoir...")
            break

    print(f"La partie est terminée, vous avez vaincu {nombre_victoires} monstre(s).")
    jouer()

# Démarrer le jeu
jouer()
