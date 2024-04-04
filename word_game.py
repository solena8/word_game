import random
from dataclasses import dataclass
from word import Word
from result import Result


@dataclass
class WordGame:
    word_to_guess: Word
    guessed_word: Word
    result: Result

    def __init__(self):
        word_list = []
        raw_list = open('List_Of_Words.txt')
        for word_str in raw_list:
            word_str = word_str.strip()
            if len(word_str) != 5:
                raise Exception(f"Word {word_str} bad length (len{len(word_str)})")
            word_list.append(Word(word=word_str))
            self.word_to_guess = random.choice(word_list)

    def propose_word(self, Word) -> Result:
        print('Devine le mot!:')
        self.guessed_word = input()
        # utiliser méthode de Word pour comparaison des deux mots guessed_word et word_to_guess
        print(self.result)

