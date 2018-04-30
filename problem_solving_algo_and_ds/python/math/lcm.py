def lcm(a, b):
    old_a = a
    while (old_a % b) != 0:
        old_a += a
    return old_a
