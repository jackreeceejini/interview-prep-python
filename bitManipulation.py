""" A collection of essential utilities and sometimes just single
powerful functions"""

def parity1(x):
    """
    Find the parity of a given number x
    The parity is the oddness or evenness of a number
    a number with an odd number of bits set 1 has odd parity
    and the function outputs 1 while even number of bits outputs
    0

    """

    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)]^
    PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK]^
    PRECOMPUTED_PARITY[(x >> MASK_SIZE)
    & BIT_MASK] ^ PRECOMPUTED_PARITY[x & BIT_MASK])


def parity2(x):
    """ 
    Using XOR to compute the parity of a 64bit number x

    """

    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1 #use the 0x1 mask to extract the last bit is the parity


def swap_bits(x, i , j):
    """
    Extract the i-th and j-th bits, and see if they differ
    """

    if (x >> i) & 1 != (x >> j) & 1:
        # if they differ we swap by flipping thier values
        # otherwise we leave them as they are
        # select the bits to flip with a bit_mask.
        # since x^1 = 0 when x = 1 and 1 when x = 0
        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x



if __name__ == "__main__":
    x = swap_bits(0b111000, 1,3)
    print("x with bit 2 and 4 swapped", bin(x))

