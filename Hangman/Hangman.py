"""
Game of hangman
"""
#     ______
#    |/     |
#    |      o
#    |     /|\
#    |     / \
# __ | __

import random

# global variables
guess_amount = 10
wordlist = []
previous_word = []
life_counter = 0
game_state = False
correct_guesses = []
all_guesses = []


# Read a file and store words in a list
def ReadFile():  #
    text_file = open('hangman-words.txt', 'r')
    file = text_file.readlines()

    for word in file:
        wordlist.append(word.strip())

    text_file.close()
    # print(wordlist)


# Reset the global variables if a new game is started
def ResetGame():
    global life_counter
    life_counter = 0
    global game_state
    game_state = False
    global correct_guesses
    correct_guesses = []
    global all_guesses
    all_guesses = []


# Sets the correct_guess list to the length of the random word
def SetGuess():
    global correct_guesses

    if len(correct_guesses) == 0:
        for i in range(len(rnd_word)):
            correct_guesses.insert(i, '')


# Gets a random word from the wordlist if it has not been used before
def GetWord():
    # get a random word
    global rnd_word
    global previous_word

    while True:
        rnd_word = random.choice(wordlist)

        if not previous_word.__contains__(rnd_word):  # if the previous word has not been used
            previous_word.append(rnd_word)  # add it to previous_word
            return True
        elif len(previous_word) == len(wordlist):  # if both lists are equal, all words are used
            return False


# Checks to see if the user has already guessed a letter or word, to stop them from using it several times
def CheckGuess(user_guess):
    if not all_guesses.__contains__(user_guess):
        all_guesses.append(user_guess)
        return False
    else:
        print('You have already guessed: {}'.format(user_guess))
        return True


# Checks word that the user has guessed
def WordGuess(user_guess):
    if user_guess == rnd_word:  # if it is the same as the random word the user has won
        Won()
        return True
    else:
        print('Incorrect word guessed')  # else increase the amount of lives used and go to draw the hangman
        global life_counter
        if life_counter < guess_amount:
            DrawHangman(life_counter)
            life_counter += 1


# Checks the letter is contained in the word and displays if it is
def LetterGuess(user_guess):
    placement = []

    if rnd_word.count(user_guess) == 1:  # if rnd_word only contains the guess letter once
        placement.append(rnd_word.find(user_guess))  # find the index of the single letter and add to placement
        if not correct_guesses.__contains__(user_guess):  # if correct_guess does not contain the single letter
            correct_guesses[placement[0]] = user_guess  # add the letter in the index that was stored in placement

    elif rnd_word.count(user_guess) >= 2:  # if rnd_word contains the guess letter >=2
        ind = 0
        for i in range(len(rnd_word)):  # for each letter in rnd_word
            if rnd_word[i] == user_guess:  # if the guess letter == rnd_word
                placement.append(i)  # add the index of the letter
                correct_guesses[placement[ind]] = user_guess  # add the letter in the index that was stored in placement
                ind += 1

    else:
        print('Incorrect letter guessed: {}'.format(user_guess))  # if the guess is incorrect
        global life_counter
        if life_counter < guess_amount:  # if life counter is < 10
            DrawHangman(life_counter)  # go to draw hangman
            life_counter += 1

    print('\nYour current guess: {}'.format(correct_guesses))  # displays the current guess

    if ''.join(correct_guesses) == rnd_word:  # check if correct_guess as string equals rnd_word
        Won()  # if equals user has won
        return True


# print the hangman in list at the index set by the life coutner
def DrawHangman(life):
    hangman = ['\n\n\n\n__ | __', '           \n    |\n    |\n    |\n    |\n __ | __',
               '     ______\n    |/     \n    |      \n    '
               '| \n    |     \n __ | __',
               '     ______\n    |/     |\n    |      \n    |     \n    |     \n __ | __', '     ______\n    |/     '
                                                                                           '|\n    |      o\n    |    '
                                                                                           ' \n    |     \n __ | __',
               '     ______\n    |/     |\n    |      o\n    |      |\n    |     \n __ | __', '     ______\n    |/    '
                                                                                              ' |\n    |      o\n    '
                                                                                              '|      |\\\n    |     '
                                                                                              '\n __ | __',
               '     ______\n    |/     |\n    |      o\n    |     /|\\\n    |     \n __ | __', '     ______\n    |/  '
                                                                                                '   |\n    |      o\n '
                                                                                                '   |     /|\\\n    | '
                                                                                                '    /   \n __ | __',
               '     ______\n    |/     |\n    |      o\n    |     /|\\\n    |     / \\\n __ | __']

    print(hangman[life])


# display user has won
def Won():
    print('You Won! You lost {} lives'.format(life_counter))


# display user has lost
def Lost():
    print('You lost, the word was: {}'.format(rnd_word))
    return True


# loop the game until the user has won or list
def GameLoop():
    global game_state
    has_guessed = True
    SetGuess()
    print('The word is: {}'.format(correct_guesses))

    while True:
        while has_guessed:  # if has guessed == false leave loop
            guess = input('\nGuess a letter or word: ')  # get user input
            guess = guess.lower().strip()

            if guess.isalpha():  # check guess is a letter only
                has_guessed = CheckGuess(guess)  # check if word has already been guessed, return true = loop continues
            else:
                print('\nInput alpha characters only')

        has_guessed = True  # reset has_guessed for next input

        if len(guess) >= 2:  # if guess length >= 2 assume it is a word guess
            game_state = WordGuess(guess)
        else:  # guess lengh == 1, letter guess
            game_state = LetterGuess(guess)

        if life_counter == guess_amount:  # if life_counter == 10, output lost and update game_state to true
            game_state = Lost()

        if game_state:  # if game_state == true, break out of GameLoop()
            break


# Start of program
if __name__ == '__main__':
    ReadFile()

    while True:
        game_state = GetWord()  # set game state to true if there is a word to guess
        if game_state:  # if game_state == true
            GameLoop()

            play = input('Do you want to play again? y/n: ')  # input to see if user wants to play again
            if play.lower() == 'y' or play.lower() == 'yes':  # if yes
                ResetGame()  # reset everything
                print('New Game\n')

            else:  # else break out of loop
                break
        else:  # if game_state == false - all the word have been guessed, break out  of the loop
            print('You have guessed all the words!')
            break
