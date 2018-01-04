"""
solution: http://stackoverflow.com/questions/727707/finding-all-combinations-of-well-formed-brackets/728051#728051

The recursion is taking advantage of the fact that you can never add more opening brackets than the desired number of pairs, and you can never add more closing brackets than opening brackets
"""
def brackets(output, opens, closes, pairs):
    if (opens == pairs) and (closes == pairs):
        print output
    else:
        if opens < pairs:
            brackets(output + "(", opens + 1, closes, pairs)
        if closes < opens:
            brackets(output + ")", opens, closes + 1, pairs)


n = 3
i = 1
while i <= n:
    brackets("", 0, 0, i)
    i += 1
