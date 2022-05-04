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

def welcome_dear_player():
    """
    Greets the player.
    Collects player name from the terminal.
    Making sure that player has only letters in his name using isalpha method,
    otherwise notifies the player about the issue.
    Coverts first letter of the players name to capital using capitalize method.
    """
    player_name = input("""<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3
Welcome to The Hangman!!! 
Please enter your name: """).capitalize()
    
    if player_name.isalpha() == True:
        print("""\nHello""", player_name, """nice to meet you! :D 

The goal of the game is to guess the
right word & not die, good luck and have fun!
<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3""") 

    else:
        print("\nOoops, it seems you haven't used only letters in your name...")
        player_name = input("Please enter your name again: ").capitalize()
        print("""\nHello""", player_name, """nice to meet you! :D
<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3""")

# constant variable which indicates the number of lives left to the player
# each life is lost by the wrong answer
LIVES = ['''
   +---+
       |
       |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
       |
      ===''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===''']