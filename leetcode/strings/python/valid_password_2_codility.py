"""
https://codility.com/programmers/lessons/90-tasks_from_indeed_prime_2015_challenge/longest_password/

You would like to set a password for a bank account. However, there are three restrictions on the format of the password:

    1. it has to contain only alphanumerical characters (a-z, A-Z, 0-9)
    2. there should be an even number of letters
    3. there should be an odd number of digits.

You are given a string S consisting of N characters. String S can be divided into words by splitting it at, and removing, the spaces. The goal is to choose the longest word that is a valid password. You can assume that if there are K spaces in string S then there are exactly K + 1 words.

For example, given "test 5 a0A pass007 ?xy1", there are five words and three of them are valid passwords: "5", "a0A" and "pass007". Thus the longest password is "pass007" and its length is 7. Note that neither "test" nor "?xy1" is a valid password, because "?" is not an alphanumerical character and "test" contains an even number of digits (zero).

Write a function:

    def solution(S)



For example, given S = "test 5 a0A pass007 ?xy1", your function should return 7, as explained above.

Assume that:

N is an integer within the range [1..200];
string S consists only of printable ASCII characters and spaces.
"""


def solution(S):
    max_length = 0
    words = [word for word in S.split(' ') if word.isalnum()]

    for word in words:
        letter_count = 0
        num_count = 0

        i = 0

        while i < len(word):

            if word[i].isdigit():
                num_count += 1
            elif word[i].isalpha():
                letter_count += 1

            i += 1

        if letter_count % 2 == 0 and num_count % 2 == 1:
            max_length = max(max_length, i)

    return -1 if max_length == 0 else max_length

print solution('test 5 a0A pass007 ?xy1')
print solution('test')
print solution('12345678')
print solution('a')
