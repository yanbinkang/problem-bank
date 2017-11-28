def fib(n):
    if n < 0:
        raise Exception("Index was negative.")
    elif n in [0,1]:
        return n

    prev = 0
    prev_prev = 1

    for index in range(n):
        current = prev + prev_prev
        prev_prev = prev
        prev = current

    return current

print fib(5)
