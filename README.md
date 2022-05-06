# THE HANGMAN

Hangman is classic word guessing game played between two or more players. In this particular case game is played against the computer. Computer sets a word and the player has to guess correctly, given a certain number of trials. For every wrongly guessed word, a life in the game is lost and a “hanging-man” begins to appear, piece by piece. The aim is to solve the puzzle and guess the correct word before the hangman dies. It's a Python terminal game, which runs in The Code Institute mock terminal on Heroku.

![Responsivness](/images-readme.md/am-i-responsive-doc.png)

## How to play

- Computer chooses random word
- A player takes an initial guess at a letter that might be contained in the word
- If the letter is contained in the word the player gains a point and takes another turn guessing a letter.
- If the letter is not contained in the word, the player losses a life, and a part of the hangman appears.
- For every wrong guess the hangman appears bit by bit until the complete image is drawn.
- Similarly, for every correctly guessed letter, the letters are placed on the screen until the word is completed and the player wins.
- Player has 6 lives

## Features

### Existing Features

- Welcomes the player
- Collects player's name, capitalize it
- Explains the goal of the game
- Shows initial picture of The Hangman game (empty gallows)
- Accepts user input
- Play against the computer
- Generates random word

![Welcome](/images-readme.md/welcome-player-doc.png)

- Input validation, error-check
  - Player must enter letter from english alphabet
  - Player can't enter the same guess multiple times
  - Player is allowed to enter only single letter
  - Player is getting notified about wrong letters

![Input validation](/images-readme.md/input-validation-error-check-doc.png)

- Game checks if player won or lost the game and prints appropriate message accordingly
- Notifies the player what the secret word was
- Asks the player if he would like to play the game again, if yes(Y,y) the game resets, if no(any other key), prints appropriate message and says good bye to the player

![Game lost](/images-readme.md/won-lost-game-doc.png)

![Game won](/images-readme.md/game-won-doc.png)

![Play again](/images-readme.md/play-again-doc.png)