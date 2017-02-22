import json
from random import randint

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
    is_input_type_letter = False

    is_input_valid = False

    #while you have less than 6 incorrect letters
    while guess_remaining - len(incorrect_letters) > 0:
      #REMOVE!!
      print(secret_word)

      #print hangman status
      self.fill_man(len(letters_guessed_array))

      #print current game stats
      self.print_game_stats(guess_remaining, secret_word, letters_guessed, incorrect_letters)

      while not is_input_valid:
        #prompt to get choice of word or letter
        letter_or_word_option = raw_input("Would you like to guess a letter or word?(Type 'L' or 'W')")
        
        #test for validity
        is_input_valid = self.isLetterOrWordValid(letter_or_word_option.upper().strip(), True)
      
      #reset is_input valid for the next validity test 
      is_input_valid = False
      
      guess_remaining -= 1

  
  def get_blanks(self, word_length):
    dashes = "";

    for i in range(word_length):
      if i == word_length:
        dashes += '_'
      else:
        dashes += '_' + ' '

    return dashes


  def print_game_stats(self, guesses_rem, word, letters_guessed, incorr_lets):
    print("\n******************************************\n")
    print("{}, you have {} guesses remaining.\n".format(self.player.user_name, guesses_rem))
    print("Your Secret Word has {} letters.\n".format(len(word)))
    print("This is what you need to finish solve: \n\n{}".format(letters_guessed))
    print("\nThese are the letters that you guessed incorrectly: {}\n".format(','.join(incorr_lets)))

  
  def fill_man(self, numTries):
    body_parts = ["-----\n     |", "     O ", "    - -", "     | ", "    / \\"]
    
    for ind in range(numTries -1 ):
      print(body_parts[ind])
  

  def isLetterOrWordValid(self, str, validify_input_type):
    if validify_input_type:
      if str == 'L' or str == 'W':
        #if input type is letter flag as true (false means input type is word)
        if str == 'L':
          is_input_type_letter = True
        return True
      else:
        return False
    else:
      #validify word or letter
      print('nothing')



    

  


    


player1 = Player("tisha")
print(player1.user_name)
tishagame = HangmanGame(player1)

tishagame.start_game()


