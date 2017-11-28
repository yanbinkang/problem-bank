"""
ref: http://www.geeksforgeeks.org/lexicographic-rank-of-a-string/
http://blog.suryaelite.com/2010/02/finding-rank-of-word-with-repetition.html
"""
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

def count_of_repeating(string):
    count = 0

    for i in range(len(string)):
        if string[i] in string[i+1:]:
            count  = 1 + string[i+1:].count(string[i])

    return count

def find_smaller_in_right(string, low, high):
    count_right = 0

    i = low + 1

    while i <= high:
        if string[i] <= string[low]:
            count_right += 1
        i += 1

    return count_right

def find_rank(string):
    str_len = len(string)
    mul = fact(str_len)
    repeat_count = count_of_repeating(string)
    repeat_count_fact = fact(repeat_count)
    rank = 1

    for i in range(str_len):
        mul = mul / (str_len - i)

        count_right = find_smaller_in_right(string, i, str_len-1)
        rank += (count_right * mul) / repeat_count_fact

    return rank

if __name__ == '__main__':
    word = 'india'
    s = 'bombay'
    print "%s" % find_rank(s)
