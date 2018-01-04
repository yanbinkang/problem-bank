"""
https://leetcode.com/problems/bulls-and-cows/

https://discuss.leetcode.com/topic/28466/python-3-lines-solution/10
"""
def get_hint(secret, guess):
    bull, cow = 0, 0

    secret_map, guess_map = {}, {}

    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bull += 1
        else:
            secret_map[secret[i]] = secret_map.get(secret[i], 0) + 1
            guess_map[guess[i]] = guess_map.get(guess[i], 0) + 1

    for key in secret_map:
        if key in guess_map:
            cow += min(secret_map[key], guess_map[key])

    return '{0}A{1}B'.format(bull, cow)

if __name__ == '__main__':
    print get_hint('1807', '7810')
    print get_hint('1123', '0111')
