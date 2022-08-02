# -*- coding: utf-8 -*-
"""
Created on Mon Aug  1 23:53:10 2022

@author: Raahim
"""

import random
from words import words
from hangman_visual import lives_visual_dict
import string


def get_valid_word(words):
    word = random.choice(words)  # randomly chooses something from the list
    while '-' in word or ' ' in word: # if the word has - or ' ' in it, ignore this and pick another word
        word = random.choice(words)
    
    return word.upper()


def hangman():
    word = get_valid_word(words)
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase) # This is set of english alphabets ( built in )
    used_letters = set()  # what the user has guessed

    lives = 7

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list))

        letter_from_user = input('Guess a letter: ').upper()
        if letter_from_user in alphabet - used_letters:
            used_letters.add(letter_from_user)
            if letter_from_user in word_letters:
                word_letters.remove(letter_from_user)
                print('')

            else:
                lives = lives - 1  # misses one lige because of wrong guess
                print('\nYour letter,', letter_from_user, 'is unfortunately not in the word.')

        elif letter_from_user in used_letters:
            print('\nYou have already used that letter. Guess another letter.')

        else:
            print('\nThat is not a valid letter. Try again')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print(lives_visual_dict[lives])
        print('You died!!! The word was', word)
    else:
        print('Hurray! You guessed it right. The word was', word, '!!')


if __name__ == '__main__':
    hangman()
    while(True):
        k = input('Press any key to exit now! If you wnat to play again press R!').upper()
        if k == 'R':
            hangman()
        else:
            break