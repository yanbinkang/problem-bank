"""
https://www.pramp.com/question/jKoA5GAVy9Sr9jGBjzN4

In this question we'll implement a function root that calculates the n'th root of a number. The function takes a nonnegative number x and a positive integer n, and returns the positive n'th root of x within an error of 0.001
"""
def root(num, n):
    if num == 0:
        return 0

    lower_bound = 0
    upper_bound = max(1, num)

    approx_root = (upper_bound + lower_bound) / 2

    while approx_root - lower_bound >= 0.001:
        if pow(approx_root, n) > num:
            upper_bound = approx_root
        elif pow(approx_root, n) < num:
            lower_bound = approx_root
        else:
            break

        approx_root = (upper_bound + lower_bound) / 2

    return approx_root
"""
We want to find a number that when mutiplied by itself n times will give us num! pow(some_number, n) does this.
"""
def root_1(num, n):
    if num == 0:
        return 0

    low = 0.0
    high = max(1, num)

    mid = (high + low) / 2

    # we need this condition to get a power that would be close to num
    while mid - low >= 0.001:
        if pow(mid, n) > num:
            # this number mid, is too high for us. We cut our search in half!
            high = mid
        elif pow(mid, n) < num:
            # this number mid, is too low for us. We cut our search in half!
            low = mid
        else:
            break

        mid = (high + low) / 2 # find mid and go again

    return mid

def root_2(num, n):
    low, high = 0.0, num

    while low < high:
        mid = (low + high) / 2

        res = pow(mid, n)

        diff = abs(num - res)

        if diff <= 0.001:
            return '%.3f' % mid
        elif res > num:
            high = mid
        else:
            low = mid


if __name__ == '__main__':
    print root(7, 3)
    print('\n')
    print root(9, 2)
    print('\n')
    print root_1(9, 2)
    print('\n')
    print root_2(4, 2)
    print('\n')
    print root_2(7, 3)
    print('\n')
    print root_2(9, 2)
    print root_2(27, 3)

