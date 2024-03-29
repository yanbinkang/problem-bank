"""
https://leetcode.com/problems/happy-number/

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 19 is a happy number

1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

https://discuss.leetcode.com/topic/19520/my-python-solution

Note: we're using a set because we don't want to compute two numbers twice. Eg. 82 and 28.
"""
def is_happy(n):
    n_set = set()

    while n != 1:
        n = sum([int(i) ** 2 for i in str(n)])

        if n in n_set:
            return False
        else:
            n_set.add(n)
    else:
        return True

def is_happy_2(n):
    n_set = set()

    while n >= 1:
        result = 0

        n_str = str(n)

        for char in n_str:
            result += pow(int(char), 2)

        if result in n_set:
            return False
        else:
            n_set.add(result)

        if result == 1:
            return True

        n = result


if __name__ == '__main__':
    print is_happy(3)
    print('\n')
    print is_happy_2(19)
