import itertools
import re

puzzle_input = 'cqjxjnds'

def get_next_password(password):
    last_char = password[-1]
    if last_char != 'z':
        return password[:-1] + chr(ord(last_char) + 1)
    return get_next_password(password[:-1]) + 'a'

def is_password_valid(password):
    if any([c in password for c in ['i', 'o', 'l']]): return False
    if (re.match(r'.*([a-z])\1.*([a-z])\2.*', password) == None): return False
    for i, c in enumerate(password[:-2]):
        if ord(c) + 1 == ord(password[i + 1]) and ord(password[i + 1]) + 1 == ord(password[i + 2]):
            return True
    return False

def get_next_valid_password(password):
    while (is_password_valid(password) == False):
        password = get_next_password(password)
    return password

password1 = get_next_valid_password(puzzle_input)
print 'First password: ' + password1
password2 = get_next_valid_password(get_next_password(password1))
print 'Second password: ' + password2
