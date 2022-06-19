import random
from words import random_words


def legitimate_word(random_words):
    word = random.choice(random_words)
    while " " in word or "-" in word:
        word = random.choice(random_words)

    return word.upper()


def welcome_dear_player():
    player_name = input("""<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3
Welcome to The Hangman!!!
Please enter your name:\n""").capitalize()

    if player_name.isalpha():
        print("""\nHello""", player_name, """nice to meet you! :D
The goal of the game is to guess the
right word & not die, good luck and have fun!
<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3""")

    else:
        print("\nOoops,it seems you haven't used only letters in your name...")
        player_name = input("Please enter your name again:\n").capitalize()
        print("""\nHello""", player_name, """nice to meet you! :D
<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3<3""")


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


ALPHABET = ("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def hangman_game(wrong_letters, correct_letters, secret_word):
    print(LIVES[len(wrong_letters)])
    print()

    print("\nWrong letters are:", end=" ")
    for letter in wrong_letters:
        print(letter, end=" ")
    print()

    gaps = "_" * len(secret_word)

    for x in range(len(secret_word)):
        if secret_word[x] in correct_letters:
            gaps = gaps[:x] + secret_word[x] + gaps[x+1:]

    for letter in gaps:
        print(letter, end=" ")


def player_speculation(guessed_already):
    while True:
        print("\nGuess a letter please:")
        guess = input()
        guess = guess.upper()
        if len(guess) != 1:
            print("Enter single letter please!")
        elif guess not in ALPHABET:
            print("Enter letter from the english alphabet please!")
        elif guess in guessed_already:
            print("Letter", guess, "has been tried already, please try again!")
        else:
            return guess


def new_game():
    response = input("\nPlay again? (Y/N): ").upper()
    print()

    if response == "Y":
        program_run()
    else:
        print("See you next time! Bye-Bye...")


def program_run():
    welcome_dear_player()
    wrong_letters = ""
    correct_letters = ""
    secret_word = legitimate_word(random_words)
    game_over = False

    while game_over is False:
        hangman_game(wrong_letters, correct_letters, secret_word)

        guess = player_speculation(wrong_letters + correct_letters)

        if guess in secret_word:
            correct_letters = correct_letters + guess

            word_completion = True
            for x in range(len(secret_word)):
                if secret_word[x] not in correct_letters:
                    word_completion = False
                    break
            if word_completion:
                print("Congrats! You're not dying today, you won the game!")
                game_over = True
            if game_over:
                if new_game():
                    wrong_letters = ""
                    correct_letters = ""
                    game_over = False
                    secret_word = legitimate_word(random_words)
                else:
                    break
        else:
            wrong_letters = wrong_letters + guess

            if len(wrong_letters) == len(LIVES) - 1:
                hangman_game(wrong_letters, correct_letters, secret_word)
                print("\nGame over, you died! Secret word was", secret_word)
                game_over = True

            if game_over:
                if new_game():
                    wrong_letters = ""
                    correct_letters = ""
                    game_over = False
                    secret_word = legitimate_word(random_words)
                else:
                    break


program_run()
