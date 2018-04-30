"""
https://leetcode.com/problems/hamming-distance/#/description

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
0 <= x, y <= 231.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)




ALGO:
read: http://python-reference.readthedocs.io/en/latest/docs/operators/bitwise_XOR.html

Counting from the front (0 index), postion 1 and 3 have different bits

Bitwise XOR sets the bits in the result to 1 if either, but not both, of the corresponding bits in the two operands is 1.

This is perfect for this question. We can take XOR of both numbers and count 1's in the result.

https://discuss.leetcode.com/topic/72288/python-1-line-49ms
"""
def hamming_distance(x, y):
    return bin(x ^ y).count('1')

if __name__ == '__main__':
    print hamming_distance(1, 4)
