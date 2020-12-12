# Hangman game
# The main goal here is to create a “guess the word” game.
# The user needs to be able to input word guesses.
# A limit (ten) should also be set on how many guesses they can use.
# When the user plays Hangman, the computer first selects a secret word
# at random from a list built into the program.
# The program then prints out a row of dashes—one for each letter
# in the secret word—and asks the user to guess a letter.
# If the user guesses a letter that is in the word,
# the word is redisplayed with all instances of that letter shown
# in the correct positions, along with any letters correctly guessed on
# previous turns. If the letter does not appear in the word,
# the user is charged with an incorrect guess.The user keeps guessing letters until either:
# (1) the user has correctly guessed all the letters in the word or
# (2) the user has made ten incorrect guesses.
# * Please use functions to modularize the code.
from random import randint
word_list = ['vehicle', 'carrot', 'school', 'puppy', 'chicken']
char_list = []
incorrect_guess_count = 0

def display_word(index):
    win = True
    for i in range(0, len(word_list[index])): #for each character in word
           if(word_list[index][i] in char_list):
               print(word_list[index][i], ' ', end = '')
           else:
               print('_ ', end = '')
               win = False
    if(win == True):
        print('')
        print("Game over. You won.")
        exit(0)
def check_guess(guess_char, index):
    # check word_list[index] & check whether guess_char is in it
    # if so, reveal those places & return true
    # if not, increment incorrect guess count & return false
    print("In check_guess()")
    if(guess_char in word_list[index]):
        char_list.append(guess)
        return True
    else:
        return False
print("Hi! Welcome to Hangman!")
rand_int = randint(0, len(word_list) - 1)

for i in range(0, len(word_list[rand_int])):
    print('_ ', end='')
for x in range(0, 10):
    print('')
    guess = input("Please enter a letter to guess: ")
    if(guess.isalpha() != True):
        print("That guess is not applicable.")
    check_guess(guess, rand_int)
    display_word(rand_int)