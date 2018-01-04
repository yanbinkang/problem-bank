import sys

def justify(words, width):
    split_words = words.split()
    n = len(split_words)
    cost = [[None for i in range(n)] for j in range(n)]

    """
    next 2 for loop is used to calculate cost of putting words from
    i to j in one line. If words don't fit in one line then we put
    sys.maxint there.
    """
    for i in range(n):
        cost[i][i] = width - len(split_words[i])
        for j in range(i+1, n):
            cost[i][j] = cost[i][j-1] - len(split_words[j]) - 1

    for i in range(n):
        for j in range(i, n):
            if cost[i][j] < 0:
                cost[i][j] = sys.maxint
            else:
                cost[i][j] = cost[i][j] ** 2


    min_cost = [0 for i in range(n)]
    result = [0 for i in range(n)]

    for i in reversed(range(n)):
        min_cost[i] = cost[i][n-1]
        result[i] = n
        j = n - 1
        while j > i:
            if cost[i][j-1] == sys.maxint:
                # continue
                # j -= 1
                cost[i][j-1] = sys.maxint
            if min_cost[i] > min_cost[j] + cost[i][j-1]:
                min_cost[i] = min_cost[j] + cost[i][j-1]
                result[i] = j
            j -= 1

    print "Minimum cost is", min_cost[0]
    print "\n"

    string = ""
    i = 0
    while True:
        j = result[i]
        k = i
        while k < j:
            string += (split_words[k] + " ")
            k += 1
        string += "\n"
        i = j
        if j >= n:
            break

    return string


if __name__ == '__main__':
    words = ["albert", "roy", "likes", "to", "code"]
    words_1 = ["Geeks", "for", "Geeks", "presents", "word", "wrap", "problem"]
    # print justify(words, 10)
    print justify("Geeks for Geeks presents word wrap problem", 15)
