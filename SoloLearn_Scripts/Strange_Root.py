# Strange Root
# A number has a strange root if its square and square rot share any digit. For example, 2 has a strange root because
# the square root of 2 equals 1.414 (consider the first three digits after the dot) and it contains 4 (which is the square
# of 2).
#
# Examples:
# Input: 11
# Output: True
# (The square root of 11 is 3.317, the square of 11 is 121. They share the same digit, 1.)
#
# Input: 24
# Output: false (the square root of 24 (4.899) and square (576) do not share any digits)
#
# Write a program to check if the user input has a strange root or not.

from math import sqrt

def check_num(num):
    square = num**2
    # squareRoot receives the num variable and passes by sqrt math function, later passes by round function,
    # limiting the float to three decimal points
    squareRoot = round(sqrt(num), 3)
    square_list = [n for n in str(square)]
    squareRoot_list = [n for n in str(squareRoot) if n != '.']

    for n1 in square_list:
        for n2 in squareRoot_list:
            if n1 in n2:
                return True
            else:
                return False

num = input('Type a Number: ')