#Damian Lefebvre
#31 aout 2023
#TP1

def count_word(input_string):
    words = input_string.split()  # Divise la chaîne en mots en utilisant l'espace comme séparateur
    return len(words)  # Retourne le nombre de mots

# Exemple d'utilisation
if __name__ == "__main__":
    text = input("Entrez une phrase : ")
    word_count = count_word(text)
    print("Le nombre de mots est :", word_count)
