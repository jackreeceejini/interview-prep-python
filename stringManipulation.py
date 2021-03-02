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
    s = '1'
    for _ in range(n - 1):
        s = ''.join(str(len(list(group))) + key for key, group in itertools.groupby(s))
    return s 

if __name__ == "__main__":
    print(look_and_say_pythonic(6))
