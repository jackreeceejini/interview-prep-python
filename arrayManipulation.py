"""
Some array manipulations

"""
import random

def even_odd(A):
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0:
            next_even += 1
        else:
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
    return A


def plus_one(A):
    """Add 1 to an array of decimal digits
    eg [1,2,9] to [1,3,0]
    """
    A[-1] += 1
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break 
        A[i] = 0
        A[i - 1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A 



def multiply(num1, num2):
    """
    multiply two numbers given as digits in a list
    eg. [2,3,5,6] * [6,3,6,3]
    """
    sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
    num1[0], num2[0] = abs(num1[0]), abs(num2[0])

    result = [0] * (len(num1) + len(num2))
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            result[i + j + 1] += num1[i] * num2[j]
            result[i + j] += result[i + j + 1] // 10
            result[i + j + 1] %= 10

    # Remove the leading zeros
    result = result[next((i for i, x in enumerate(result)
    if x != 0), len(result)):] or [0]

    return [sign * result[0]] + result[1:]

def generate_primes(n):
    init = [False]*2 +[True] * (n - 1)
    primes = []
    for p in range(2,  n + 1):
        if init[p]:
            primes.append(p)
            for i in range(p, n + 1, p):
                init[i] = False
    return primes

def random_sampling(k, A):
    """
    generate a random sampling of A
    """
    for i in range(k):
        # Generate a random index in [i, len(A) - 1]
        r = random.randint(i, len(A) - 1)
        A[i], A[r] = A[r], A[i]
    return A

def compute_random_permutation(n):
    permutation = list(range(n))
    random_sampling(n, permutation)
    return permutation


def random_subset(n, k):
    changed_elements = {}
    for i in range(k):
        # Generate a random index between i and n - 1, inclusive
        rand_idx = random.randrange(i, n)
        rand_idx_mapped = changed_elements.get(rand_idx, rand_idx)
        i_mapped = changed_elements.get(i, i)
        changed_elements[rand_idx] = i_mapped
        changed_elements[i] = rand_idx
    return [changed_elements[i] for i in range(k)]



if __name__ == "__main__":
    print(random_subset(9,5))
    
