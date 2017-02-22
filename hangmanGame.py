import json #json module
import re #regular expression module
import sys
from random import randint #to genenerate random number
from datetime import datetime #to generate time


#Create dictionary of Words
with open('./dictionary/dictionaryWords.json') as json_data:
    dictionary_words = json.load(json_data)

dictionary = dictionary_words['words']
dict_length = len(dictionary)

################################ Player Class ################################
class Player():
  def __init__(self, user_name):
    self.user_name = user_name
    self.num_of_wins = 0
    self.time_of_last_win = None


############################# Hangman Game ##################################
class HangmanGame():
  def __init__(self, player):
    self.player = player
    self.max_guesses = 6

  def start_game(self):
    guess_remaining = self.max_guesses
    random_num = randint(0, dict_length)
    self.secret_word = dictionary[random_num].upper()
    self.incorrect_letters_array = []
    self.incorrect_words_array = []

    self.letters_guessed_array = self.get_blanks().split(' ')
    
    #flag for input type(letter or word)
    self.this_input_type_is_letter = False

    is_input_valid = False

    self.this_user_guess_response = None
    num_guesses_so_far = 0
    num_correct_guesses_so_far = 0;

    #while you have less than 6 incorrect letters
    while guess_remaining > 0:
      #REMOVE ME!!
      print(self.secret_word)
      
      
      print("\n******************************************\n")
      #print hangman status
      self.fill_man(num_guesses_so_far)
      letters_guessed = ' '.join(map(str, self.letters_guessed_array))
      incorrect_letters_guessed = ', '.join(map(str, self.incorrect_letters_array))
      incorrect_words_guessed  = ', '.join(map(str, self.incorrect_words_array))
      #print current game stats
      self.print_game_stats(guess_remaining, letters_guessed, incorrect_letters_guessed, 
                            incorrect_words_guessed)

      #prompt user for choice of input type and validify input
      while not is_input_valid:
        #prompt to get choice of word or letter
        letter_or_word_option = raw_input("Would you like to guess a letter or word?(Type 'L' or 'W')")
        
        #test for validity
        is_input_valid = self.is_letter_or_word_valid(letter_or_word_option.strip().upper(), True)
      
      #reset is_input valid for the next validity test 
      is_input_valid = False

      #simple formatting for output
      if self.this_input_type_is_letter:
        input_type = "letter"
      else:
        input_type = "word"
      
      
      #prompt user for letter or word and validify input
      while not is_input_valid:
        print("Remember all characters must contain letters only")
        #prompt user for the word or letter that they want to guess
        letter_or_word_guess = raw_input("Please guess a {}\n".format(input_type))

        #validate input matches input type (false means we want to test if input a valid word/letter)
        is_input_valid = self.is_letter_or_word_valid(letter_or_word_guess.strip().upper(), False)

      #if input is word, test word to see if it matches secret word
      if not self.this_input_type_is_letter:
        if self.this_user_guess_response == self.secret_word:
          self.user_wins_game()
          # brake or end game?
        else:
          # incorrect response. Since this is a word add to incorrect words array
          print("You entered an incorrect word")
          self.incorrect_words_array.append(self.this_user_guess_response)
      else:
        #input is a letter
        #Check to see how many of letters are in the word
        indices_of_letter = self.get_indices_of_letter_in_word()

        #update correct letters guessed so far to determine win
        num_correct_guesses_so_far += len(indices_of_letter)

        
        if(len(indices_of_letter)): 
          #change dashes to letters for correct letter guessed
          self.change_dashes_to_letters(indices_of_letter)
        else:
          #add letter to incorrect guessed letters arrayr
          self.incorrect_letters_array.append(self.this_user_guess_response)

      #test to see if user wins game
      if num_correct_guesses_so_far == len(self.secret_word):
        self.user_wins_game()
      #need to reset input type and response for next iteration
      is_input_valid = False
      self.this_input_type_is_letter = False
      self.this_user_guess_response = None
      guess_remaining -= 1
      num_guesses_so_far += 1

  #This method gets all instances of position of letter guessed in secret word
  def get_indices_of_letter_in_word(self):
    letter_indices = []

    for i, ltr in enumerate(self.secret_word):
      if ltr == self.this_user_guess_response:
        letter_indices.append(i)

    return letter_indices


  #Replaces dashes to letters of respective index and returns string with indices and dashes
  def change_dashes_to_letters(self, indices):
    for i in indices:
        self.letters_guessed_array[i] = self.this_user_guess_response


  #This method prints dashes on start of game. The dashes represent the number of letters in secret word
  def get_blanks(self):

    dashes = ""
    for i in range(len(self.secret_word)):
      if i == len(self.secret_word) - 1:
        dashes += "_";
      else:
        dashes += "_" + " "
  
    return dashes;

  #This method prints the game statistics
  def print_game_stats(self, guesses_rem, letters_guessed, incorr_lets, incorr_words):
    print("\n******************************************\n")
    print("{}, you have {} guesses remaining.\n".format(self.player.user_name, guesses_rem))
    print("Your Secret Word has {} letters.\n".format(len(self.secret_word)))
    print("This is what you need to finish solve: \n\n{}".format(letters_guessed))
    print("\nThese are the letters that you guessed incorrectly: {}\n".format(incorr_lets))
    print("\nThese are the words that you guessed incorrectly: {}\n".format(incorr_words))

  #This method will be used to print fill in the body parts of the hangman diagram
  def fill_man(self, numTries):
    body_parts = ["-----", "     |", "     O ", "    - -", "     | ", "    / \\"]
    
    for ind in range(numTries):
      print(body_parts[ind])
  

  #This method will be used to test both the validity of input type chosen by user and validity 
  # validity of letter or word
  def is_letter_or_word_valid(self, str, validify_input_type):
    if validify_input_type:
      if str == 'L' or str == 'W':
        #if input type is letter flag as true (false means input type is word)
        if str == 'L':
          self.this_input_type_is_letter = True
        return True
      else: 
        return False
    else:
      #validify word or letter
      allLetters = '^[A-Za-z]+$'

      #if string is not all letters
      if not re.match(allLetters, str):
        return False

      #if string entered is a letter
      if len(str) is 1:
        if self.this_input_type_is_letter:
          self.this_user_guess_response = str
          return True
        else:
          #string entered is a letter, but we are expecting a word
          return False
      else:
        #string entered is a word
        if not self.this_input_type_is_letter:
          self.this_user_guess_response = str
          return True 
        else:
          #string entered is a word, but we are expecting a letter
          return False

  def user_wins_game(self):
    print("YooHoo! you won! The correct word was '{}'".format("".join(self.letters_guessed_array)))
    #update user stats for database
    self.player.num_of_wins += 1
    self.player.time_of_last_win = datetime.now()
    #add user to list of winners
    self.end_game()

  def end_game(self):
    sys.exit()



    

  


    


player1 = Player("tisha")

tishagame = HangmanGame(player1)

tishagame.start_game()


