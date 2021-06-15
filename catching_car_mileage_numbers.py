# https://www.codewars.com/kata/52c4dd683bfd3b434c000292/train/python

def is_interesting(number, awesome_phrases):
    # Error checking
    if number < 98:
        return 0
    if number > 999999999:
        return 0

    if number > 99:
        if has_trailing_zeros(number):
            return 2
        
        if all_digits_same(number):
            return 2

        if digits_are_incrementing(number):
            return 2

        if digits_are_decrementing(number):
            return 2

        if digits_are_palindrome(number):
            return 2
        
        if number_matches_phrase(number, awesome_phrases):
            return 2

    for n in range(1,3):
        if has_trailing_zeros(number+n):
            return 1
    
        if all_digits_same(number+n):
            return 1

        if digits_are_incrementing(number+n):
            return 1

        if digits_are_decrementing(number+n):
            return 1

        if digits_are_palindrome(number+n):
            return 1
        
        if number_matches_phrase(number+n, awesome_phrases):
            return 1

    return 0

def has_trailing_zeros(number):
    return (number / 100).is_integer()

def all_digits_same(number):
    string = str(number)
    if len(string) < 3:
        return False
    first_digit = string[0]
    return string.count(first_digit) == len(string)

# THIS METHOD CREATES A VALUEERROR EXCEPTION WHEN RUNNING RANDOM TESTS ON CODEWARS
def digits_are_incrementing(number):
    string = str(number)
    for digit in string[1:]:
        if digit == '0':
            digit = '10'
        if int(digit) - int(string[string.index(digit) - 1]) == 1:
            continue
        else:
            return False
    return True

def digits_are_decrementing(number):
    string = str(number)
    for digit in string[1:]:
        # if digit == 0:
        #     digit = 10
        if int(string[string.index(digit) - 1]) - int(digit) == 1:
            continue
        else:
            return False
    return True

def digits_are_palindrome(number):
    string = str(number)
    return string == string[::-1]

def number_matches_phrase(number, awesome_phrases):
    return number in awesome_phrases

# print(digits_are_palindrome(121))
# print(digits_are_decrementing(321))
# print(digits_are_incrementing(67890))
# print(all_digits_same(222))
# print(has_trailing_zeros(100))
print(is_interesting(122, [1337, 256]))