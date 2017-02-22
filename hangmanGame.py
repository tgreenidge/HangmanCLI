import json
from random import randint
import re

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


############################# Hangman Game ##################################
class HangmanGame():
  def __init__(self, player):
    self.player = player
    self.max_guesses = 6

  def start_game(self):
    guess_remaining = self.max_guesses
    random_num = randint(0, dict_length)
    secret_word = dictionary[random_num]
    incorrect_letters = []

    #fix this
    letters_guessed_array = []

    #fix this
    #letters_guessed = ','.join(letters_guessed_array)

    
    letters_guessed = self.get_blanks(len(secret_word))
    
    #flag for input type(letter or word)
    self.this_input_type_is_letter = False

    is_input_valid = False

    self.this_user_guess_response = None

    #while you have less than 6 incorrect letters
    while guess_remaining - len(incorrect_letters) > 0:
      #REMOVE ME!!
      print(secret_word)

      #print hangman status
      self.fill_man(len(letters_guessed_array))

      #print current game stats
      self.print_game_stats(guess_remaining, secret_word, letters_guessed, incorrect_letters)

      #prompt user for choice of input type and validify input
      while not is_input_valid:
        #prompt to get choice of word or letter
        letter_or_word_option = raw_input("Would you like to guess a letter or word?(Type 'L' or 'W')")
        
        #test for validity
        is_input_valid = self.is_letter_or_word_valid(letter_or_word_option.strip().upper(), True)
      
      #reset is_input valid for the next validity test 
      is_input_valid = False

      #test
      print("Here", self.this_input_type_is_letter)
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

      print(" Your input is valid")


      guess_remaining -= 1

  #This method prints dashes on start of game. The dashes represent the number of letters in secret word
  def get_blanks(self, word_length):
    dashes = "";

    for i in range(word_length):
      if i == word_length:
        dashes += '_'
      else:
        dashes += '_' + ' '

    return dashes

  #This method prints the game statistics
  def print_game_stats(self, guesses_rem, word, letters_guessed, incorr_lets):
    print("\n******************************************\n")
    print("{}, you have {} guesses remaining.\n".format(self.player.user_name, guesses_rem))
    print("Your Secret Word has {} letters.\n".format(len(word)))
    print("This is what you need to finish solve: \n\n{}".format(letters_guessed))
    print("\nThese are the letters that you guessed incorrectly: {}\n".format(','.join(incorr_lets)))

  #This method will be used to print fill in the hangman status
  def fill_man(self, numTries):
    body_parts = ["-----\n     |", "     O ", "    - -", "     | ", "    / \\"]
    
    for ind in range(numTries -1 ):
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




  def end_game(self):
    pass



    

  


    


player1 = Player("tisha")
print(player1.user_name)
tishagame = HangmanGame(player1)

tishagame.start_game()


