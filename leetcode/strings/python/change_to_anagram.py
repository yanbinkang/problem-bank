"""
https://www.hackerrank.com/contests/101june13/challenges/anagram/problem

Sid loves to read short stories. Being a Computer Science student, he decides to do some frequency analysis on his favorite reading material. For each data point, chooses a string of length a from one book, and a string of length b from a second book. The strings' lengths differ by no more than 1.
|a-b| <= 1, where |x| represents the absolute value function.

The frequency analysis consists of checking how far the strings are from being anagrams of one another. Your challenge is to help him find the minimum number of characters of the first string he needs to change to make it an anagram of the second string. He can neither add nor delete characters from the first string. Only replacement of the characters with new ones is allowed.
Input Format


The first line will contain an integer T representing the number of test cases. Each test case will contain a string having length (a+b) which will be concatenation of both the strings described in problem. The string will only contain small letters and without any spaces.
Output Format
An integer corresponding to each test case is printed in a different line i.e., the number of changes required for each test case. Print "-1" if it is not possible.


Constraints:

1 <= a + b < 10,000

Sample Input

5
aaabbb
ab
abc
mnop
xyyx


Sample Output
3
1
-1
2
0


1. One string must be "aaa" and the other "bbb". The lengths are a=3 and b=3, so the difference is less than 1. No characters are common between the strings, so all three must be changed.

2. One string must be "a" and the second "b". The lengths are a=1 and b=1, so the difference is less than 1. One character must be changed to them the same.


3. Since the string lengths a and b must differ by no more than 1, the lengths are either a=1 and b=2 or a=2 and b=1. No sequence of substitutions will make the two  anagrams of one another.

4. One string must be "mn" and other be "op". The length are a=2 and b=2, so the difference is less than 1. No characters are common between the strings, so both must be changed.


5. One string must be "xy" and the other be "yx". The length are a=2 and b=2, so the difference is less than 1. No changes are needed because the second string is already an anagram of the first.


algo:  Check if they are valid string. If length == odd, then fail, -1
Use int[26] arr to add chars from s1. If non-26-char exist, return -1
use same int arr to remove chars from s2.
count the non-zeros
"""
def change_to_anagram(word):

    if len(word) % 2 == 1: return -1

    mid = len(word) / 2

    left, right = word[:mid], word[mid:]

    col = [0] * 26

    for i in range(len(left)):
        l = left[i]
        r = right[i]

        col[ord(l) - ord('a')] += 1
        col[ord(r) - ord('a')] -= 1

    count = 0

    for num in col:
        count += abs(num)

    return count // 2

if __name__ == '__main__':
    assert 10 == change_to_anagram('hhpddlnnsjfoyxpciioigvjqzfbpllssuj')

    assert 13 == change_to_anagram('xulkowreuowzxgnhmiqekxhzistdocbnyozmnqthhpievvlj')

    assert 5 == change_to_anagram('dnqaurlplofnrtmh')

    assert 26 ==  change_to_anagram('aujteqimwfkjoqodgqaxbrkrwykpmuimqtgulojjwtukjiqrasqejbvfbixnchzsahpnyayutsgecwvcqngzoehrmeeqlgknnb')

    assert 15 == change_to_anagram('lbafwuoawkxydlfcbjjtxpzpchzrvbtievqbpedlqbktorypcjkzzkodrpvosqzxmpad')

    assert -1 == change_to_anagram('drngbjuuhmwqwxrinxccsqxkpwygwcdbtriwaesjsobrntzaqbe')

    assert 3 == change_to_anagram('ubulzt')

    assert 13 == change_to_anagram('vxxzsqjqsnibgydzlyynqcrayvwjurfsqfrivayopgrxewwruvemzy')

    assert 13 == change_to_anagram('xtnipeqhxvafqaggqoanvwkmthtfirwhmjrbphlmeluvoa')

    assert -1 ==  change_to_anagram('gqdvlchavotcykafyjzbbgmnlajiqlnwctrnvznspiwquxxsiwuldizqkkaawpyyisnftdzklwagv')
