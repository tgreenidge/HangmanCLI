//--------------------- Dictionary -------------------------------\\
//Dictionary for game play. Check Json file for details of restrictions of words in dictionary
var dictionary = require('./dictionary/dictionaryWords').words;


//required to read the response from the user interface
var readline = require('readline');

var rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});


//--------------------- Player constructor ----------------------------------\\
var Player = function(username, name){
  this.username = username;
  this.name = name;
};

//REMOVE Me!!
//history of players. Acts like a database May change this
var registeredPlayers = {};
var winners = {};
/*******************************************************************/

//--------------------- Hangman Game constructor -------------------------------\\

var HangmanGame = function(player, gameOption){
  this.maxGuesses = 6;
  this.player = player;
  this.gameOption = gameOption;
};

//starts the actual game play and continues until the game comes to an end
HangmanGame.prototype.startGame = function(){
  // TO DO change main based on option!!!!!

  var guessesRemaining = this.maxGuesses;
  
  //generate random number to correspond with index of word in dictionary
  var randomNumber = Math.floor((Math.random() * dictionary.length));
  
  //secretWord for this game
  this.secretWord = dictionary[randomNumber];

  //Use this to get time elapsed
  this.statTime = new Date();
  
  while(guessesRemaining){
    rl.write("You have "+  guessesRemaining + " guesses remaining.\n");


    guessesRemaining--;
  }

};

HangmanGame.prototype.printRules = function(winner){
  //write rules to the console
  
};

HangmanGame.prototype.printLeaderBoard = function(){
  //
}

HangmanGame.prototype.endGame = function(winner){
  if(winner){
    console.log("You Won!");
  }else{
    console.log("Game Over!");
  }
  
}


//Game components 
  //Timer/clock - time elapsed = Time start - time now
  //player
  //word
  //guesses



// Print dashes on screen that corresponds with word length
HangmanGame.prototype.printDashes = function (word){
  var letters = document.getElementById("word-display");
  var dashes = "";

  for(var i = 0; i < word.length; i++){
    if(i === word.length -1){
      dashes += "_";
    }else{
      dashes += "_" + " ";
    }
  } 
  letters.innerHTML = dashes;
};

//Determines the indices of all letter occurances in a word
HangmanGame.prototype.getIndicesOfLetterInWord = function(word, letter){
  var letterIndices = [];

  for(var i = 0; i < word.length; i++){
    if(word[i] === letter.toLowerCase()){
      letterIndices.push(i);
    }
  }

  return letterIndices;
};

//Replaces dashes to letters of respective index and returns string with indices and dashes
HangmanGame.prototype.changeDashesToLetters = function(word, indices, letter){
  var displayedChars = document.getElementById("word-display");
  var displayedText = displayedChars.innerText.split("");
  
  for(var i = 0; i < indices.length; i++){
    if(indices[i] === 0){
      displayedText[i] = letter.toUpperCase();
    }else {
      displayedText[indices[i] * 2] = letter.toUpperCase();
    }
  }
  
  return displayedText.join("");
}

//Displays the string as either the correct letters in word or incorrectly guessed letters on DOM
HangmanGame.prototype.displayLetters = function(str, isCorrectLetter){
  var textContent;

  if(isCorrectLetter){
    textContent= document.getElementById("word-display");
  } else {
    textContent= document.getElementById("letters-guessed-display");
  }

  textContent.innerHTML = str;
};

HangmanGame.prototype.drawMan = function(numTries){
  var bodyParts = ["-----\n     |","     O ", "    - -","     | ", "    / \\"];
  for(var i = 1; i <= numTries; i++){
    console.log(bodyParts[i - 1]);
  }
}


//REMOVE ME
// // use the following template
// rl.write("Type 'help' for commands\n");
// rl.write("Square numbers:\n");

//--------------------- create new Game -------------------------------\\
function createNewHangmanGame(){
  //Create player object from input of user - prompt for username and name
//var username = ("Please enter your username");
//var player1 = new Player(username, name);


  
}


var player = new Player("Tisha", "Tisha");
var newGame = new HangmanGame(player);
newGame.startGame();

