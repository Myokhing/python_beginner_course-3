import random
from words import words
import string
#print(words)
def get_valid_word(words):
    word = random.choice(words) # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word
def hangman():
        word = get_valid_word(words)
        word_letters = set(word) # letter in the word
        alphabet = set(string.ascii_uppercase)
        used_letters = set() #what the user has guessed
        lives = 6
        #getting user input
        while len(word_letters) > 0 and lives > 0:
            #letters used
            print('You have', lives, 'these letters:', ' '.join(used_letters))
            #what current word is (ie W- R D)
            word_list = [letter if letter in used_letters else '-' for letter in word]
            print('current word:', ' '.join(word_list))
            user_letter = input('Guess a letter:').upper()
            if user_letter in alphabet - used_letters:
                used_letters.add(user_letter)
                if user_letter in word_letters:
                    word_letters.remove(user_letter)
                else:
                    lives = lives -1  #take away a life if wrong
                    print('Letter is not in word.')
            elif user_letter in used_letters:
                print('You have already used that character. please try again.')
            else: 
                print('Invalid character. please try again.')
        #get here when len(word_letters) == 0 OR when lives == 0
        if lives ==0:
            print('You died, sorry. the word was', word)
        else:
            print('Yoy guessed the word', word, '!!')
hangman()

