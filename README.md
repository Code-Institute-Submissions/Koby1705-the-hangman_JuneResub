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