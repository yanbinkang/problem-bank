def parity(x):
    """
    compute the parity of a binary word. The parity of a binary word is 1 if the number if 1s in the word is odd; otherwise, it is 0.
    """
    result = 0
    while x:
        result ^= x & 1
        x >>= 1

    return result

if __name__ == '__main__':
    print parity(8)
