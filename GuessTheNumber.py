"""
user decides range of randomly generated number
user decides amount of guesses they would like
user guesses the number
store and display previous guesses
tell the user if it their number is higher or lower than the random number
"""
import random

# Get lower value, check it is a digit
while True:
    val = input('Enter the lower value of the number range: ')
    try:
        lowerVal = int(val)
    except ValueError:
        print('Use numeric digits')

    if val.isdigit():
        break

# Get upper value, check it is a digit and larger than the lowerVal
upperVal = 0
while True:
    val = input('Enter the upper value of the number range: ')

    try:
        upperVal = int(val)
    except ValueError:
        print('Use numeric digits')

    if upperVal > lowerVal and val.isdigit():
        break

print('You set the lower value as {} and upper value as {}' .format(lowerVal, upperVal))

# Get the guess amount, check it is a digit
while True:
    val = input('How many guesses would you like? ')

    try:
        guessAmount = int(val)
    except ValueError:
        print('Use numeric digits')

    if val.isdigit():
        break

number = random.randint(lowerVal, upperVal)  # Generate random number
# print('DEBUG: random number', number)

game_state = 0
win = False
prevGuess = []

# While the state is less than the defined guessAmount
while game_state < guessAmount:
    # Get the guess input, check it is a digit and it is within the lower and upper val range
    while True:
        try:
            guess = input('{}. Guess the number between {} and {}: '.format(game_state + 1, lowerVal, upperVal))
            numGuess = int(guess)
        except ValueError:
            print('Use numeric digits')

        if guess.isdigit():
            if lowerVal <= numGuess <= upperVal:
                break
            else:
                print('Your guess does not fit in your defined range')

    prevGuess.append(numGuess)  # Store the guess

    if numGuess == number:
        print('You guessed correct, the random number was ', number, '\n')
        win = True
        break

    if numGuess > number:
        print('Your guess is greater than the random number\n')

    if numGuess < number:
        print('Your guess is less than the random number\n')

    print('Previous Guesses: ', prevGuess)
    game_state += 1

if win:  # True
    print('Well done you guessed the random number in ', game_state + 1, ' guesses')
else:  # False
    print('You did not guess the number! It was ', number, '!')
