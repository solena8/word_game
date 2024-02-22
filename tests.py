from word import Word
from word_game import Word_Game

# Instantiate Word_Game
word_game_1 = Word_Game()

# Call the give_a_random_word method on the instance
word_game_1.give_a_random_word()

# Access and print the randomly chosen word stored in word_to_guess attribute
print(word_game_1.word_to_guess)