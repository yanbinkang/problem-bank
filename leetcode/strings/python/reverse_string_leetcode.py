"""
https://leetcode.com/problems/reverse-string/?tab=Description

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".

https://discuss.leetcode.com/topic/43296/java-simple-and-clean-with-explanations-6-solutions
"""
def reverse_string(s):
    s = list(s)
    first = 0
    last = len(s) - 1

    while first < last:
        # temp = s[first]
        # s[first] = s[last]
        # s[last] = temp
        s[first], s[last] = s[last], s[first]

        first += 1
        last -= 1

    return ''.join(s)

if __name__ == '__main__':
    print(reverse_string('hello'))
    print(reverse_string('leetcode'))

