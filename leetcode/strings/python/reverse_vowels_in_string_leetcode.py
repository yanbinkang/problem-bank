"""
https://leetcode.com/problems/reverse-vowels-of-a-string/?tab=Description

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".

algorithm: similar to quick sort partition sub-routine!

O(n) time O(n) space

https://discuss.leetcode.com/topic/43412/java-standard-two-pointer-solution
"""
def reverse_vowels(s):
    vowels = 'aeiouAEIOU'
    s = list(s)

    first = 0
    last = len(s) - 1

    done = False

    while not done:
        while first <= last and s[first] not in vowels:
            first += 1

        while last >= first and s[last] not in vowels:
            last -= 1

        if last < first:
            done = True
        else:
            temp = s[first]
            s[first] = s[last]
            s[last] = temp

        first += 1
        last -= 1

    return ''.join(s)

if __name__ == '__main__':
    print reverse_vowels('hello') #holle
    print reverse_vowels('leetcode') #leotcede
    print reverse_vowels('aA') #Aa

