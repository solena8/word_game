import random
from dataclasses import dataclass
from word import Word


@dataclass
class Word_Game:
    word_list: list[Word]
    word_to_guess: Word
    guessed_word: Word


    def __init__(self):
        self.word_list = []
        raw_list = open('List_Of_Words.txt')
        for word in raw_list:
            self.word_list.append(word)

    def give_a_random_word(self) -> str:
        self.word_to_guess = random.choice(self.word_list)
        return self.word_to_guess




    # Donne moi un mot (qui ne s'affiche pas)
    # divise le en 5 lettres
    # je donne un mot (qui s'affiche)
    # on compare chaque lettre du mot 1 au mot 2
    # Si la lettre est la même == True
        # + afficher la lettre correcte ligne à la suivante (couleur verte)
    # Si non :
        # Checher dans le mot 1 si la lettre du mot 2 existe ailleurs
            # Si oui :
                # afficher la lettre mal placée entre parenthèses à la ligne suivante (couleur jaune)
            # Si non :
            #     afficher un espace à la place de la lettre incorrecte à la ligne suivante