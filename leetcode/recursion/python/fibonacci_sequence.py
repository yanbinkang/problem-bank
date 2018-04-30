# https://youtu.be/UxICsjrdlJA?list=PL2_aWCzGMAwLz3g66WrxFGSXvSsvyfzCO
"""
Rule for calculating fibonacci sequence with memoization:

1. Set base case

2. check if n is in the cache before making a recursive call! If it is return the value

3. save the value of the recursive call in the cache with key as n and value as the result

4. Return the result of above step from the cache.
"""
d = {}
def fib_with_memo(n):
    if n <= 1:
        return n

    # check cache if we've already done this calculation before making another recursive call!
    if n in d:
        return d[n]

    d[n] = fib_with_memo(n - 1) + fib_with_memo(n - 2) # store the result

    return d[n] # return the result

    """
    OR
    f = fib_with_memo(n - 1) + fib_with_memo(n - 2)
    d[n] = f
    return d[n]

    We could also get rid of the base case:
    if n <= 1: return n

    and instead initialize d[0] = 0; d[1] = 1 which will take care of the base case
    """

def fib_iterative(n):
    f1 = 0
    f2 = 1

    for i in range(2, n + 1):
        f = f1 + f2
        f1 = f2
        f2 = f

    return f2

def fib_bottom_up(n):
    table = [None] * (n + 1)

    table[0] = 0
    table[1] = 1

    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[n]



if __name__ == '__main__':
    print fib_with_memo(45)
    print fib_iterative(45)
    print fib_bottom_up(45)
