


/****************************** Global Variables *****************************************/

//--------------------------- User Interface ------------------------------\\
//required to read the response from the user interface (the command line)
var readline = require('readline');

var rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
  
//-----------------------------User Interface Helper Functions --------------------------------\\
//Processes input for user's choice to entering a letter or a word
function validateLetterOrWordInputOption(str){
  var isValid;
  var isLetter;
  
  //make string case insenstive
  str = str.toUpperCase().trim();
  
  if(str === 'L' || str === 'W') {
    isValid = true;
    if(str === 'L'){
      //user wants to enter a letter
      isLetter = true;
    }else{
      //user wants to enter a word
      isLetter = false;
    };
  }else{
    isValid = false;
  }

  return [isValid, isLetter];
}

function promptUserForLetterOrWordOption (callback) {
  rl.question("\nDo you want to guess a letter or guess a word? (Type 'L' or 'W')\n", function(answer){
    var response = validateLetterOrWordInputOption(answer);
    callback(response);
  });
}

function processLetterOrWordOption(arr) {
  if(!arr[0]){
    promptUserForLetterOrWordOption(processLetterOrWordOption);
  }else{
    promptUserToGuessLetterOrWord(arr[1]);
  }
}

function promptUserToGuessLetterOrWord (isLetter) {
  if(isLetter){
    console.log("You want to guess a letter");
  }else{
    console.log("You want to guess a word");
  }
}




//--------------------- Dictionary for hangman Game--------------------------\\
//Dictionary for game play. Check Json file for details of restrictions of words in dictionary
var dictionary = require('./dictionary/dictionaryWords').words;


//------------------------------ Rules for game--------------------------------\\
var rules = {

};

//--------------------------------Menu for game------------------------------\\
//This is a list of options user has before/after/during game play
var menu = {

}

//-------------------------------- Game Options ----------------------------------\\
//This is list of choices that user has to play the game. 

var gameOptions = {

}


//--------------------- Player constructor ----------------------------------\\
var Player = function(username, name){
  this.username = username;
  this.name = name;
};

//----------------------Registered Players -------------------------------------\\
//Decide where to store this
//REMOVE Me!!
//history of players. Acts like a database May change this
var registeredPlayers = {};
var winners = {};
/******************************************************************************************/



/******************************Hangman Game ***********************************************/

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
  var secretWord = dictionary[randomNumber];

  //Use this to get time elapsed
  this.startTime = new Date();
  
  var lettersGuessedSofar = this.getBlankDashes(secretWord);
  var incorrectLetters = [];
  
  //change thise... need to do for 1
  while(guessesRemaining === 6){

    this.fillMan(incorrectLetters.length);
    //print User Statistics
    this.printStatistics (this.player.name, 
                          guessesRemaining, 
                          secretWord, 
                          lettersGuessedSofar, 
                          incorrectLetters.join(','));
    
    // user for choice to enter a letter or a word, then process the option for next prompt
    // if user does not type L, or W (not case senstive), user is asked to enter L or W again
    // otherwise, user should receive prompt to enter guess
    
    promptUserForLetterOrWordOption(processLetterOrWordOption);





    //if guess is wrong 
    //call this.fill man

    guessesRemaining--;
    rl.write(incorrectLetters.length);
  }

  // if(!guessesRemaining){
  //   this.fillMan(this.maxGuesses - guessesRemaining);
  // }

};

HangmanGame.prototype.printRules = function(){
  //!!!!! need a call back
  console.log(rules);
  
};

HangmanGame.prototype.printLeaderBoard = function(){
  //
}

//d
HangmanGame.prototype.endGame = function(winner){
  if(winner){
    console.log("You Won!");
  }else{
    console.log("Game Over!");
  }
  
}


// Print blank dashes on screen that corresponds with word length
HangmanGame.prototype.getBlankDashes = function (word){
  var dashes = "";

  for(var i = 0; i < word.length; i++){
    if(i === word.length -1){
      dashes += "_";
    }else{
      dashes += "_" + " ";
    }
  } 
  
  return dashes;
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

HangmanGame.prototype.fillMan = function(numTries){
  var bodyParts = ["-----\n     |","     O ", "    - -","     | ", "    / \\"];
  for(var i = 1; i <= numTries; i++){
    console.log(bodyParts[i - 1]);
  }
}

HangmanGame.prototype.printStatistics = function(name, guessesRem, word, lettersGuessed, incorrLets){
  console.log("\n******************************************\n");
  console.log(name + ", you have "+  guessesRem + " guesses remaining.\n");
  console.log("Your Secret Word has " + word.length + " letters.\n"); // add this to menu instructions 
  console.log("This is what you need to finish solve: \n\n" + lettersGuessed);
  console.log("\n\nThese are the letters that you guessed incorrectly:" + incorrLets);    
}










//REMOVE ME
// // use the following template
// rl.write("Type 'help' for commands\n");
// rl.write("Square numbers:\n");
// function createPayer(number, callback){
//     rl.question("Enter player " + number + " name? ", function(answer) {
//         var player = new Player(answer);

//         // Call the callback function once the player is created.
//         callback(player);
//     });
// }

//--------------------- create new Game -------------------------------\\
function createNewHangmanGame(){
  //Create player object from input of user - prompt for username and name
//var username = ("Please enter your username");
//var player1 = new Player(username, name);


  
}


var player = new Player("Tisha", "Tisha");
var newGame = new HangmanGame(player);
newGame.startGame();
//console.log(newGame.printDashes("test"));

