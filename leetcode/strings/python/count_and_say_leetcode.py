"""
https://leetcode.com/problems/count-and-say

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

O(n * m) time where n is the integer given and m is the size of string at step n.

O(m) space where m is the size of the string at step n
"""
def count_and_say(n):
    seq = '1'

    # start from 1 because we've already initialized seq = '1'
    for i in range(1, n):
        string = ''
        count = 1

        for j in range(1, len(seq)):
            if seq[j] == seq[j - 1]:
                count += 1
            else:
                string += str(count) + seq[j - 1]
                count = 1

        """
        seq = '1' i.e we're starting or we've reached the last index for seq.

        When we're starting we need to go to '11'. This allows us to do so.

        Also, say seq = '1211'. When you get to the last element of 1 (index 3), string will be '1112'. Count will be 2 and we need to add that and the last element to the result. So we do seq = '1112' + '2' + '1' which is equivalent to the code below!
        """
        seq = string + str(count) + seq[-1]

    return seq

def count_and_say_1(n):
    s = '1'

    for i in range(1, n):
        count = 1
        string = ''

        for j in range(1, len(s) + 1):
            # end of the string or char and previous char are not the same
            if j == len(s) or s[j - 1] != s[j]:
                string += str(count)
                string += s[j - 1]
                count = 1
            else: # char and previous char are the same
                count += 1

        s = string
    return s


if __name__ == '__main__':
    print count_and_say(5)
    print count_and_say_1(5)

