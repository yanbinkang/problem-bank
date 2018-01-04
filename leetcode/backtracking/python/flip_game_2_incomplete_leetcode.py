"""
https://leetcode.com/problems/flip-game-ii/#/description

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

For example, given s = "++++", return true. The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Follow up:
Derive your algorithm's runtime complexity.
"""

def canWin(s):
    """
    :type s: str
    :rtype: bool
    """
    # result = []
    d = {}

    return helper(s, d)

def helper(s, d):
    if s not in d:
        for i in range(1, len(s)):
            if s[i] == '+' and s[i - 1] == '+':
                t = s[:i - 1] + '--' + s[i + 1:]
                # result.append( s[:i - 1] + '--' + s[i + 1:] )
                if not helper(t, d):
                    d[s] = True
                    return True

        d[s] =  False
        return False

if __name__ == '__main__':
    print canWin('++++')
    print canWin('--++----++')
