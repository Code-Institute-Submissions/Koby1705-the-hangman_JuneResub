# import the random module
import random
# from file words.py gets english list of words stored in random_words variable
from words import random_words


def legitimate_word(random_words):
    """
    Making sure that words from the list with dashes and white spaces are eliminated.
    Chooses random, valid word from a list and converts all lowercase characters
    in a string into uppercase characters.
    """
    word = random.choice(random_words)
    while " " or "-" in word:
        word = random.choice(random_words)

    return word.upper()