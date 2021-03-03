"""
Solutions to string manipulation problems
"""

import string
import functools
import itertools

def is_palindromic(s):
    return all(s[i] == s[~i] for i in range(len(s)//2))

def int_to_string(x):
    is_negative = False
    if x < 0:
        x, is_negative = -x, True
    
    s = []
    while True:
        s.append(chr(ord('0') + x % 10))
        x //= 10
        if x == 0:
            break

    # adds negative sign back if is_negative
    return ('-' if is_negative else '') + ''.join(reversed(s))

def string_to_int(s):
    return functools.reduce(lambda running_sum, c :running_sum * 10 + string.digits.index(c),
    s[s[0] == '-':],0) * (-1 if s[0] == '-' else 1)


def convert_base(num_as_string, b1, b2):
    """
    Covert a number given as a string from one base (b1) to another (b2)
    """
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else
            construct_from_base(num_as_int // base, base) + 
            string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else 
        construct_from_base(num_as_int, b2))

def look_and_say_pythonic(n):
    """
    n is a number from 1 to max Integer
    """
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + key for key, group in itertools.groupby(s))
    return s 

def roman_to_integer(s):
    """
    s is a string made up of roman numerals
    """
    T = {'I' : 1, 'V' : 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}

    return functools.reduce(
        lambda val, i: val + (-T[s[i]] if T[s[i]] < T[s[i + 1]] else T[s[i]]),
        reversed(range(len(s) - 1)), T[s[-1]])

def get_valid_ip_address(s):
    """
    s is a string of integer digits from which all
    valid ip addresses will be generated
    
    e.g. 19216811 -> 192.168.1.1
    """
    def is_valid_part(s):
        # '00', '000', '01', etc. are not valid, but '0' is valid.
        return len(s) == 1 or (s[0] != '0' and int(s) <= 255)
    result, parts = [], [None] * 4
    for i in range(1, min(4, len(s))):
        parts[0] = s[:i]
        if is_valid_part(parts[0]):
            for j in range(1, min(len(s) - i, 4)):
                parts[1] = s[i:i+j]
                if is_valid_part(parts[1]):
                    for k in range(1, min(len(s) - i - j, 4)):
                        parts[2], parts[3] = s[i + j:i + j + k],s[i + j + k:]
                        if is_valid_part(parts[2]) and is_valid_part(parts[3]):
                            result.append('.'.join(parts))
    return result

if __name__ == "__main__":
    print(get_valid_ip_address('19216811'))
