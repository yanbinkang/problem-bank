"""
https://leetcode.com/problems/number-of-1-bits/#/description

Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer '11' has binary representation 00000000000000000000000000001011, so the function should return 3.
"""
def hamming_weight(n):
    return bin(n).count('1')

def hamming_weight_1(n):
    return len([i for i in range(32) if (1 << i) & n])


if __name__ == '__main__':
    print hamming_weight(11)
    print hamming_weight_1(11)
