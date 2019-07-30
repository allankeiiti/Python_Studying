from string import ascii_lowercase, ascii_uppercase
import re

def validate_length(password):
    if (len(password) >= 5 and len(password) <= 10):
        return True
    if (len(password) < 5):
        error_message = 'The Password Length is less than 5 limit'
    if (len(password) > 10):
        error_message = 'The Password Length is more than 10 limit'
    return error_message

def validate_lowerAndUpperCase(password):
    has_Upper = False
    has_Lower = False
    for letter in password:
        if letter in ascii_uppercase:
            has_Upper = True
        if letter in ascii_lowercase:
            has_Lower = True
    if not has_Upper:
        error_message = '\nThe Password does not have Uppercase Letter'
    if not has_Lower:
        error_message = '\nThe Password does not have Lowercase Letter'
    return error_message

def validate_numbers(password):
    error_message = '\nThe Password does not have Special Characters' if not re.match("^[a-zA-Z0-9_]*$", password)
    print(error_message)

def validate_space(password):
    if ' ' in password:
        error_message = '\nThe Password does not have Spaces'
    return error_message

