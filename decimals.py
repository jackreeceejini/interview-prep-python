""" Problems about decimal sequences"""

import math
import random


def reverse(x):
    """
    Reverse the input decimal digits
    """

    result, x_remaining = 0, abs(x)
    while x_remaining:
        result = result * 10 + x_remaining % 10
        print("result", result)
        x_remaining //= 10
        print("x_remaining", x_remaining)
    return -result if x < 0 else result


def is_palindrome_number(x):
    if x <= 0:
        return x == 0
    num_digits = math.floor(math.log10(x)) + 1
    msd_mask = 10**(num_digits - 1)
    for i in range(num_digits // 2):
        if x // msd_mask != x % 10:
            return False
        x %= msd_mask #remove the most significant digit of x
        x //= 10 # remove the least significant digit of x
        msd_mask //= 100
    return True


def uniform_random(lower_bound, upper_bound):
    """
    a uniform random number generator
    """
    number_of_outcomes = upper_bound - lower_bound + 1
    while True:
        result, i = 0, 0
        while (1 << i) < number_of_outcomes:
            result = (result << 1) | random.randint(0,1)
            i += 1
        if result < number_of_outcomes:
            break
    return result + lower_bound




if __name__ == "__main__":
    for i in range(5):
        print(uniform_random(1,6))


