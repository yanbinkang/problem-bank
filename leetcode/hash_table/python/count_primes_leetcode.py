"""
https://leetcode.com/problems/count-primes/

https://discuss.leetcode.com/topic/13654/my-simple-java-solution

https://www.youtube.com/watch?v=eKp56OLhoQs
"""
def count_primes(n):
    count = 0
    is_prime = [False] * n

    for i in range(2, n):
        if is_prime[i] == False:
            count += 1

            j = i
            while i * j < n:
                is_prime[i * j] = True
                j += 1

    return count

def count_primes_alt(n):
    if n <= 1: return 0

    not_prime = [False] * n
    not_prime[0] = True
    not_prime[1] = True

    for i in range(2, int(n ** 0.5) + 1):
        if not_prime[i] == False:
            j = i
            while j * i < n:
                not_prime[i * j] = True
                j += 1

    count = 0
    for i in range(2, len(not_prime)):
        if not_prime[i] == False:
            count += 1

    return count


if __name__ == '__main__':
    print count_primes(5)
    print count_primes_alt(5)
