"""
A game of Rock Paper Scissors
The player chooses the game amounts, inputs their move
The computer generates a random move
Results are compared
Winner announced
Rock > Scissors
Scissors > Paper
Paper > Rock
if the same = draw
"""
import random

score = [0, 0]


def scoreUpdate(player):
    if player == 'player':
        score[0] = score[0] + 1
    else:
        score[1] = score[1] + 1


moves = ['Rock', 'Paper', 'Scissors']
computer = 'computer'
player = 'player'

# Player inputs amount of games, checks if its a digit
while True:
    turns = input('How many games do you want to play? ')
    try:
        if turns.isdigit:
            turns = int(turns)
            break
    except ValueError:
        print('Use numeric digits')


game_state = 0

while game_state < turns:
    compMove = random.choice(moves)
    correctInput = False

    while not correctInput:
        playerMove = input('Choose Rock, Paper, Scissors: ')
        # print('DEBUG: player move: {}'.format(playerMove))

        if playerMove.isalpha():  # Check player inputted only alphas
            # Reformat word
            playerMove = playerMove.lower()
            playerMove = playerMove.capitalize()
            # print('DEBUG: reformatted player move: {}'.format(playerMove))

            # Check if the player input is in the array, if not then it is not valid
            for move in moves:
                if playerMove == move:
                    correctInput = True
                    break
            else:
                print('{} is not a valid move'.format(playerMove))
        else:
            print('Enter letters only')

    print('Computer chose: {}'.format(compMove))

    if compMove == playerMove:
        print('Draw! You both chose {}. Neither get a point'.format(compMove))
    elif compMove == 'Rock' and playerMove == 'Scissors':
        print('Computer chose Rock and won!')
        scoreUpdate(computer)
    elif compMove == 'Scissors' and playerMove == 'Paper':
        print('Computer chose Scissors and won!')
        scoreUpdate(computer)
    elif compMove == 'Paper' and playerMove == 'Rock':
        print('Computer chose Paper and won!')
        scoreUpdate(computer)
    elif playerMove == 'Rock' and compMove == 'Scissors':
        print('Player chose Rock and won!')
        scoreUpdate(player)
    elif playerMove == 'Scissors' and compMove == 'Paper':
        print('Player chose Scissors and won!')
        scoreUpdate(player)
    elif playerMove == 'Paper' and compMove == 'Rock':
        print('Player chose Paper and won!')
        scoreUpdate(player)
    else:
        print('How did you get here?!')

    game_state += 1

    print(score)

# Get winner
if score[0] > score[1]:
    print('You won against the computer!')
elif score[0] < score[1]:
    print('You lost against the computer.')
else:
    print('You drew against the computer.')