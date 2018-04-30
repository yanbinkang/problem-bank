def count_bits(x):
    """
    program to count the number of bits that are set to 1 in a positive integer
    """
    num_bits = 0

    while x:
        num_bits += x & 1
        x >>= 1

    return num_bits

if __name__ == '__main__':
    print count_bits(12)
    print count_bits(161)

