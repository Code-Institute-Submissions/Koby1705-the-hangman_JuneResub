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
Please enter your name:\n""").capitalize()
    
    if player_name.isalpha() == True:
        print("""\nHello""", player_name, """nice to meet you! :D 

The goal of the game is to guess the
right word & not die, good luck and have fun!
<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3""") 

    else:
        print("\nOoops, it seems you haven't used only letters in your name...")
        player_name = input("Please enter your name again:\n").capitalize()
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


def hangman_game(wrong_letters, correct_letters, secret_word):
    """
    This function prints the board of the hangman game depending of how many lives
    player still has.
    Function also shows how many letters player has correctly and incorecctly guessed.
    """
    print(LIVES[len(wrong_letters)])
    print("\nWrong letters are:")
    # iterates over each letter in the string wrong_letters
    for letter in wrong_letters:
        print(letter)
    print()

    # secret word is displayed with the gaps(underscores)
    gaps = "_" * len(secret_word)

    # loop goes through each letter in secret_word and replaces the underscore
    # with the existing letter in correct_letters
    for x in range(len(secret_word)):
        if secret_word[x] in correct_letters:
            gaps = gaps[:x] + secret_word[x] + gaps[x+1:]

    for letter in gaps:
        print(letter)


def player_speculation(guessed_already):
    """
    Function ensures that only single letter from english alphabet
    can be entered.
    """
    while True:
        guess = input("Guess a letter please:\n").upper()
        if len(guess) != 1:
            print("Enter single letter please!")
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print("Enter letter from the english alphabet please!")
        elif guess in guessed_already:
            print("Letter", guess, "has been tried already, please try again!")
        else:
            return guess


def new_game():
    """
    Function returns True if player wants to play again, if not it will return False.
    """
    print("Play again? (Y/N)")
    return input().upper().startswith("y")


def program_run():
    """
    Calls the welcome_dear_player function to greet the player and collect player's name.
    Allows the player to speculate and enter the letter.
    Checks if player completed the whole secret word.
    """
    welcome_dear_player()
    secret_word = legitimate_word(random_words)
    wrong_letters = " "
    correct_letters = " "
    game_over = False

    while True:
        hangman_game(wrong_letters, correct_letters, secret_word)

        guess = player_speculation(wrong_letters + correct_letters)
        
        if guess in secret_word:
            correct_letters = guess + correct_letters
            word_completion = True
            for x in range(len(secret_word)):
                if secret_word[x] not in correct_letters:
                    word_completion = False
                    break
            if word_completion:
                print(" Congrats! You're not dying today, you won the game!")
                game_over = True
        else:
            wrong_letters = guess + wrong_letters
