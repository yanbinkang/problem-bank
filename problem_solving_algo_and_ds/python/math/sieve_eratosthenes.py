def eratosthenes(end, start=2):
    if start < 2:
        start = 2
    primes = range(start, end)
    marker = 2

    while marker < end:
        for i in xrange(marker, end + 1):
            if marker*i in primes:
                primes.remove(marker*i)
        marker += 1
    return primes


print eratosthenes(20)
