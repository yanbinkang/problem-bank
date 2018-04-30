"""
https://leetcode.com/problems/text-justification/description/

Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Note: Each word is guaranteed not to exceed L in length.

ref: https://discuss.leetcode.com/topic/25970/concise-python-solution-10-lines

algo:

How does it work?

Well, in the question statement, the sentence "Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right" was just a really long and awkward way to say round robin. The following line implements the round robin logic:

    for i in range(max_width - num_of_letters):
        cur[i % (len(cur) - 1 or 1)] += ' '


What does this line do? Once you determine that there are only k words that can fit on a given line, you know what the total length of those words is num_of_letters.

Then the rest are spaces, and there are (maxWidth - num_of_letters) of spaces. The "or 1" part is for dealing with the edge case len(cur) == 1


why do we need 'or 1'? eg. if cur = ['to'], [i % (len(cur) - 1 or 1)] will be [i % 0 or 1]. But i % 0 will result in ZeroDivisionError. So we use i % 1

Explanation:

    if num_of_letters + len(w) + len(cur) > max_width:
        pass

    num_of_letters => number of letters we've seen so far

    num_of_letters + len(w) => above, plus the current word we're looking at

    num_of_letters + len(w) + len(cur) => above, plus possible number of spaces between the words in cur

"""
def full_justify(words, max_width):
    res, cur, num_of_letters = [], [], 0

    for w in words:
        if num_of_letters + len(w) + len(cur) > max_width:
            for i in range(max_width - num_of_letters):
                cur[i % (len(cur) - 1 or 1)] += ' '

            res.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)

    return res + [' '.join(cur).ljust(max_width)]

if __name__ == '__main__':
    print full_justify(['This', 'is', 'an', 'example', 'of', 'text', 'justification.'], 16)
    print('\n')
    print full_justify([''], 0)
    print('\n')
    print full_justify(['Listen','to','many,','speak','to','a','few.'], 6)
    print('\n')
    print full_justify(['Tushar', 'Roy', 'Likes', 'To', 'Code'], 10)
