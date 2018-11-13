"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/#/description

Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.
"""
def reverse_words(s):
    s = s.split()
    result = ''

    for string in s:
        result += string[::-1] + ' '

    return result.strip()

def reverse_words_1(s):
    s = list(s)
    index = 0

    for i in range(len(s) + 1):
        if i == len(s) or s[i] == ' ':
            reverse_char(s, index, i - 1)
            index = i + 1


    return ''.join(s)

def reverse_char(s, first, last):
    while first <= last:
        temp = s[first]
        s[first] = s[last]
        s[last] = temp

        first += 1
        last -= 1

def reverse_words_2(s):
    return ' '.join([x[::-1] for x in s.split()])


if __name__ == '__main__':
    print(reverse_words("Let's take LeetCode contest"))
    print('\n')
    print(reverse_words_1("Let's take LeetCode contest"))
    print('\n')
    print(reverse_words_2("Let's take LeetCode contest"))

