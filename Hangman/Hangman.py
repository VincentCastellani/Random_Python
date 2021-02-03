"""
Game of hangman
gets a list of words from a text file
chooses a random word
get the word length, indicate the word length with -
the user guesses a letter or word
if they get the letter right they will guess again
if they get the letter wrong, they will guess again but 1 life is lost
    the hangman is drawn out
if they guess the correct word, they win
if they guess the wrong word, they will guess again but 1 life is lost
    the next hangman part is drawn out

Normal mode - 11 guesses - draws stand and body
Hard mode - 6 guesses - draws body only

- read file
- choose random word
- get user input and validate
- check input is one letter or word
- check letter is in the word and its placement
- output result
- check if the word is correct
- output result
- separate method for drawing hangman
"""
#    ______
#   |/     |
#   |      o
#   |     /|\
#   |     / \
# __ | __

import random

def wordguess(userguess):
    if userguess == word:
        print('won')
    else:
        hangmanpiece()



def letterguess(userguess):
    result = userguess
    return result

def hangmanpiece():
    #switch case statement here?
    hangman = ['    _______', '   |/     |', '   |/     |', '   |      o', '   |     /|\\', '   |     / \\', '__ | __']
    print(hangman[incorrectamount])

# open file and put words into a list
textfile = open('hangman-words.txt', 'r')
file = textfile.readlines()

wordlist = []
for word in file:
    wordlist.append(word.strip())

textfile.close()
# print(wordlist)

# get a random word
word = random.choice(wordlist)
print(word)

# get word length and tell the user
wordlengh = len(word)
print('The word length is {}'.format(wordlengh))
for i in range(wordlengh):
    print('_', end=' ')

print('\n')
while True:
    guess = input('Guess a letter or word: ')
    guess = guess.lower()


    if guess.isalpha():  # validate guess input
        if len(guess) == 1:
            letterguess(guess)
        elif len(guess) == wordlengh:
            wordguess(guess)

        else:
            print('Input a letter or the whole word')
    else:
        print('guess must be alphas only')


