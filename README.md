# HangmanCLI
This is a command line version of the popular game Hangman, built with NodeJS. Initially, I wanted to create a Web Application that would allow me to utilize JavaScript/Nodejs, Databases, and Sockets. I however experienced some issues with working with the asynchronous nature of node, with respect to ensuring the receipt of data before moving on to the next step of the game loop. In the interest of time with respect to the deadline of the project, I switched to working on this Command Line Application, with hopes of debugging and completing the web app at a later time.


### Web App version
An web app game is currently in development, and can be forked or cloned from [github](https://github.com/tgreenidge/Hangman) or played [online](https://hangman-extreme.herokuapp.com/).

# Instructions to get app running on local machine

- Clone project or fork from this repository
- Install [nodejs](https://nodejs.org/en/)
- Install [npm](http://blog.npmjs.org/post/85484771375/how-to-install-npm)
- Install game dependencies

- In the root folder of the Hangman project in the command line, type:

 ```npm install```

- Start the node server from the root folder:
  
  ```node hangmanGame```


#### Instructions to create  a different list of words that is found in the dictionaryWords.js file
   
1. Manipulate the parameters for the API to select your preferences
 
API: http://linkedin-reach.hagbpyjegb.us-west-2.elasticbeanstalk.com/words
 
Parameters: See document online for parameters to be passed into string query

- From the root folder of the project, type the following in the command line:

``` node dictionary.js ```

- This will replace the file in the **dictionary** folder called **dictionaryWords.js**


# Game Play

## Game Rules
- The player plays against the computer 
- The computer choses a word
- If the player does not guess correctly under 6 tries, the computer wins
- On each try, player can guess either a letter or a word
- On each try, if the answer is incorrect, an actual hangman diagram is displayed as it gets filled
 

### Guesses
If player tries to solve the answer by guessing the word:
  - If the word is correct, the player wins the game
  - If the word is incorrect, no letters are revealed in the answer

If player tries to solve the answer by guessing one letter at a time:
  - Correct letters in the answer are revealed in their correct positions
  - Incorrect letter guesses are displayed

### Word Lengths 
- The words are of 4 to 8 letters only

## Leader Board
Ranks players based on number of correctly solved words average time to solve challenges.


# Game Work Flow

  * Place Image Here

# Techology Stack
- Node.js
- Github

Waffle.io was also used as a project management tool to keep track of requirements, bugs, and other issues

# Challenges
- Getting user input

# Reflection
This program may have been easily implemented in another language like Ruby or Python, since those
languages facilitate user input. Since the Ruby and Python's processes would have been more synchronous in natutre, I would have written less lines of code, because a lot of the additional helper functions that were created just to process the user input would not have been necessary.

