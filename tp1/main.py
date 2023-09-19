#Damian Lefebvre
#31 aout 2023
#TP1

#definir le conteur de mots
def count_word(input_string):
    #input pour le savoir le nombre de mots
    words = input_string.split()
    #dit le nombre de mots
    return len(words)

# Exemple d'utilisation
if __name__ == "__main__":
    #demande
    text = input("Entrez une phrase : ")
    #conter
    word_count = count_word(text)
    #print resultat
    print("Le nombre de mots est :", word_count)
