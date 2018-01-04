"""
ref: http://www.geeksforgeeks.org/lexicographic-rank-of-a-string/
ref: http://blog.suryaelite.com/2010/01/finding-rank-of-word-no-repetition.html

general: the number of words that can be created using letters of a word is factorial of length of string. eg if given 'string' the ans is 6! = 6 * 5 * 4 * 3 * 2 * 1 = 720

algorithm:
1) take first char in given string and find number of chars after it which are smaller than this char.
2) multiply above result by factorial of len(given_str) - 1 and save result
3) perform above steps for all other chars in string (note that at each step lenght of string will reduce)
4) return accumulated result.

"""
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)


def find_smaller_in_right(string, low, high):
    count_right = 0

    i = low + 1

    while i <= high:
        if string[i] < string[low]:
            count_right += 1
        i += 1

    return count_right

def find_rank(string):
    str_len = len(string)
    mul = fact(str_len)
    rank = 1

    for i in range(str_len):
        mul = mul / (str_len - i)

        count_right = find_smaller_in_right(string, i, str_len-1)

        rank += count_right * mul

    return rank


if __name__ == '__main__':
    word = 'string'
    print "%s" % find_rank(word)
