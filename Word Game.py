import random
import nltk

nltk.download('words')
from nltk.corpus import words

word_list = set(words.words())

Five_letter_words = []
for word in word_list:
    if len(word) == 5 and not word[0].isupper():
        Five_letter_words.append(word)

print(random.choice(Five_letter_words))
