from unidecode import unidecode


def normalize_word(word):
    # Normalize the word by removing accents and converting to lowercase
    return unidecode(word).lower()


def supprimer_doublons_et_similaires(mots):
    # Normalize all words in the list
    mots = [normalize_word(word) for word in mots]

    # Supprimer les doublons
    mots_uniques = list(set(mots))

    # Supprimer les mots ayant les 3 premières lettres identiques
    mots_filtres = [mot for mot in mots_uniques if len(mot) < 3 or len(set(mot[:3])) != 1]

    return mots_filtres


# Ouvrir le fichier et lire son contenu
with open('List_Of_Words.txt', 'r', encoding='utf-8') as file:
    contenu_fichier = file.read()

# Diviser le contenu du fichier en une liste de mots
liste_mots = contenu_fichier.split()

# Appeler la fonction pour supprimer les doublons et les mots similaires
resultat = supprimer_doublons_et_similaires(liste_mots)

# Afficher chaque mot sur une nouvelle ligne
for word in resultat:
    print(word)
