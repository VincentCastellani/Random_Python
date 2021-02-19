"""
user inputs a password
it has to meet the requirements:
at least 8 characters
upper and lower case
letters and numbers
at least one special character (cannot use < >)

doing this to learn regex
"""
import re  # regex

if __name__ == '__main__':
    while True:
        regex = r"([a-zA-z]+)"

        password = input('Input your password: ')
        print(password)

        pattern = re.compile(regex)
        res = pattern.match(password)
        if res is None:
            print('Password is not valid')
        else:
            print('Your password is valid')

        cont = input('Do you want to check another password y/n: ')
        if cont.__contains__('n' or 'no'):  # end program if n or no is inputted
            break
