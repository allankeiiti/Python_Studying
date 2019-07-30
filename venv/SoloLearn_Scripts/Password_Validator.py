# Password Validator is a program that validates passwords to match specific rules. For example, the minimum
# length of the password must be 8 characters long and it should have at least one uppercase letter in int.
# A valid password is the one that conforms to the following rules:

# - Minimum length is 5;
# - Maximum length is 10;
# - Should contain at least one number;
# - Should contain at least one special character (such as &, +, @, $, #, %, etc)
# - Should not contain spaces;

# Examples: Input: "Sololearn" Output: False
# Input: "John Doe" Output: False
# Input: "$ololearn7" Output: True

from __init__ import validate_lowerAndUpperCase, validate_length, validate_numbers, validate_space

class user:
    def __init__(self, login, password, error_message = ''):
        self.login = login
        self.password = password
        self.error_message = error_message


user1 = user('allan.nakakita','senhA')
print(user1.login)
