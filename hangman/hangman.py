import random
import string
from hangman_words import words

def get_valid_word(words):
        word = random.choice(words)
        while '-' in words or ' ' in words:
            word = random.choice(words)
        return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 9

    while len(word_letters) > 0 and lives > 0:
        
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word is: ", ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
            else:
                lives -= 1
                print(f'Letter is not in these word. Current lives: {lives}')
                
        elif user_letter in used_letters:
            print("Your already use that letter. Please try again ")
        else:
            print('\nThat is not a valid letter')
    if lives == 0:
        print("You loose, sorry, the word is: ", word)
    else:
        print("You guessed the word correctly! The word is: ", word)
hangman()