"""
Write a function to generate the generalized abbreviations of a word.
 Example:
 Given word = "word", return the following list (order does not matter):
 ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

 https://leetcode.com/problems/generalized-abbreviation/

 The idea is: for every character, we can keep it or abbreviate it. To keep it, we add it to the current solution and carry on backtracking. To abbreviate it, we omit it in the current solution, but increment the count, which indicates how many characters have we abbreviated. When we reach the end or need to put a character in the current solution, and count is bigger than zero, we add the number into the solution.

 https://discuss.leetcode.com/topic/32270/java-backtracking-solution
"""

def generalized_abbreviation(word):
    result = []

    if not word: return ['']

    helper(word, result, 0, '', 0)

    return result

def helper(word, result, pos, string, count):
    if len(word) == pos:
        # Once we reach the end, append string to the result
        result.append(string + str(count) if count > 0 else string)
        # if count > 0:
        #     result.append(string + str(count))
        # else:
        #     result.append(string)
    else:
        # Skip current position, and increment count
        helper(word, result, pos + 1, string, count + 1)
        # Include current position, and zero-out count
        helper(word, result, pos + 1,
              string + (str(count) if count > 0 else '') + word[pos], 0)


# https://discuss.leetcode.com/topic/32765/java-14ms-beats-100
def generalized_abbreviation_alt(word):
    result = []
    if not word: return ['']

    dfs_util(result, word, '', 0, 0)

    return result

def dfs_util(result, word, string, pos, count):
    if len(word) == pos:
        if count != 0:
            result.append(string + str(count))
        else:
            result.append(string)
    else:
        dfs_util(result, word, string, pos + 1, count + 1)

        if count != 0:
            string += str(count)

        dfs_util(result, word, string + str(word[pos]), pos + 1, 0)


if __name__ == '__main__':
    print generalized_abbreviation('word')
    print('\n')
    print generalized_abbreviation_alt('word')
