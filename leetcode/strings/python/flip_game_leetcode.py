"""
https://leetcode.com/problems/flip-game/#/description

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

For example, given s = "++++", after one move, it may become one of the following states:

[
  "--++",
  "+--+",
  "++--"
]

If there is no valid move, return an empty list [].

solution: https://discuss.leetcode.com/topic/27172/ac-python-one-line-44-ms-solution
"""
def generate_possible_next_moves(s):
    """
    :type s: str
    :rtype: List[str]
    """
    return [s[:i] + '--' + s[i+2:] for i in range(len(s) - 1) if s[i:i+2] == '++']


"""
ref: https://discuss.leetcode.com/topic/27277/simple-solution-in-java

We start from i = 1 and check whether current and previous characters of the input string equals to +. If true, then add substring to a list: characters before previous one (concatenating with --) and characters after the current character.
"""
def generate_possible_next_moves_1(s):
    result = []

    for i in range(1, len(s)):
        if s[i] == '+' and s[i - 1] == '+':
            result.append( s[:i - 1] + '--' + s[i + 1:] )

    return result

print generate_possible_next_moves_1('++++')
