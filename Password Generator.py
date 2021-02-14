"""
generate password with:
- 8-20 characters
- upper and lower case letters
- numbers
- special characters

randomly choose a number between 8 and 20
choose random amount to become letters from the alphabet
choose random amount to become upper case
if there are enough character spaces left
    choose random amount to become numbers
if there are enough character spaces left
    choose random number to become special characters

jumble the password up
"""
import random
import string  # string.ascii_letters has upper and lower case

pass_min = 8
pass_max = 20


# get a random password length
def RandomNumber(min_val, max_val):
    rnd = random.randint(min_val, max_val)
    return rnd


# get random letters of random length that is <= the chosen password length
def Letters(max_val):
    letters = []
    rnd = RandomNumber(0, max_val)

    for i in range(0, rnd):
        letters.append(random.choice(string.ascii_letters))

    return letters


# get random numbers of random length that is <= the remainder of the password length
def Numbers(max_val):
    numbers = []
    rnd = RandomNumber(0, max_val)

    for i in range(0, rnd):
        numbers.append(random.randint(0, 9))

    return numbers


# get random special characters of length <= the remainder of the password length
def Special(max_val):
    special_chars = []

    for i in range(0, max_val):
        char = random.choice(string.punctuation)
        if char != '<' or char != '>':
            special_chars.append(char)

    return special_chars


# add all of the list together and shuffle them
def Jumble(list_letters, list_numbers, list_special):
    password = list_letters + list_numbers + list_special
    random.shuffle(password)
    return password


if __name__ == '__main__':
    rand = RandomNumber(pass_min, pass_max)

    password_letters = Letters(rand)

    num_remainder = rand - len(password_letters)  # check if password_letters has any space left
    if num_remainder >= 0:
        password_numbers = Numbers(num_remainder)

    special_remainder = num_remainder - len(password_numbers)  # check if password_numbers has any space left
    if special_remainder >= 0:
        password_special = Special(special_remainder)

    generated_password = Jumble(password_letters, password_numbers, password_special)

    password = ''.join(str(i) for i in generated_password)  # join the list together as string
    print('Your password is : {}'.format(password))

    #This can all be done in one line!
    one_line_password = ''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for n in range(pass_min, pass_max)])
    print(one_line_password)
