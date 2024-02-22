import random
from dataclasses import dataclass
from word import Word


@dataclass
class WordGame:
    word_list: list[Word]
    word_to_guess: Word
    guessed_word: Word

    def __init__(self):
        self.word_list = []
        raw_list = open('List_Of_Words.txt')
        for word_str in raw_list:
            word_str += ' ' * (5 - len(word_str))
            word_obj = Word(letter1=word_str[0], letter2=word_str[1], letter3=word_str[2], letter4=word_str[3],
                            letter5=word_str[4])
            self.word_list.append(word_obj)

    def give_a_random_word(self) -> Word:
        self.word_to_guess = random.choice(self.word_list)
        return self.word_to_guess
