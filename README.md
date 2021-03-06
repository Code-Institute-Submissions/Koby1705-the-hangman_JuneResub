# THE HANGMAN

Hangman is classic word guessing game played between two or more players. In this particular case game is played against the computer. Computer sets a word and the player has to guess correctly, given a certain number of trials. For every wrongly guessed word, a life in the game is lost and a “hanging-man” begins to appear, piece by piece. The aim is to solve the puzzle and guess the correct word before the hangman dies. It's a Python terminal game, which runs in The Code Institute mock terminal on Heroku.

Live link for the site can be found here: https://the-hangman-1705.herokuapp.com/

![Responsivness](/images-readme.md/am-i-responsive-doc.png)

# Contents Table

1. [**How to play**](#how-to-play)
   
2. [**Features**](#features)
   - [**Existing Features**](#existing-features)

3. [**Testing**](#testing)
   - [*Bugs*](#bugs)
     - [*Solved Bugs*](#solved-bugs)
     - [*Unsolved Bugs*](#unsolved-bugs)
     - [Validator Testing](#validator-testing)

4. [**Deployment**](#deployment)

5. [**Credits**](#credits)
   - [**Code**](#code)

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

## Testing

I have manually tested the project doing the following:
- Passed the code through PEP8 linter and confirmed there are no problems, only irrelavant minor issues which don't affect the code
- Given invalid inputs: same input twice, single letter input, inputs from english alphabet
- Tested in my local Gitpod terminal & the Code Institute Heroku terminal

### Bugs

#### Solved Bugs

- Game was starting with picture No.2 instead No.1 (empty gallows) in the list. 
  - Simple fix by deleting empty space between quotation marks in wrong_letter & correct_letters variables
- After completing the game I had to press extra random letter to finish the game instead automatic completion of the game after the win
  - I had to change while loop in program_run function from True to False by adding variable game_over and declare it to False

#### Unsolved Bugs

- No remaining unsolved bugs

#### Validator Testing

- PEP8
  - No errors returned from [pep8online.com](http://pep8online.com/)

## Deployment
Project was deployed using Code Institute's mock terminal for Heroku

- Steps:
  - Create a new Heroku app
  - Set the buildbacks to Python & NodeJS in that order
  - Link Heroku app to the repository using Gitpod terminal
    - heroku login -i
    - enter personal email
    - enter pasword using API Key from Heroku
    - heroku git:remote -a "name of the app from Heroku"
    - git push heroku main

## Credits

- Code Institute for the deployment terminal
- Scott & Gemma from tutor support who helped me and pointed me to right direction to solve some issues with my code

### Code

- Inspiration for the game was taken from few sources [Youtube.com](https://www.youtube.com/watch?v=m4nEnsavl6w) & [Youtube.com](https://www.youtube.com/watch?v=wmSysRui0cI&t=48s) & [Youtube.com](https://www.youtube.com/watch?v=cJJTnI22IF8) & [Chapter8](https://inventwithpython.com/invent4thed/chapter8.html) & [LearnPythonThroughProjects](https://mardiyyah.medium.com/a-simple-hangman-learnpythonthroughprojects-series-10-fedda58741b)