import random
import string
from words import words

def get_valid_word(words):
    print('Selecting a word')
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    print('Word Selected')
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word) # Letters in the word

    alphabet = set(string.ascii_uppercase)

    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        # Letters used
        print('You have',lives,'lives, You have used these letters:', ' '.join(used_letters))

        # What current word is (ie. W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives -= 1  # Take away a life if wrong
                print('Letter is not in word')
        elif (user_letter in used_letters):
            print('You have already used that letter. Please try again')
        else:
            print('Invalid character. Please try again')
    
    if (lives == 0):
        print('You died, sorry, the word was', word)
    else:
        print('Congratulations, You guessed the word', word)


if __name__ == '__main__':
    hangman()