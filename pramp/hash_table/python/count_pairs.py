"""
https://www.geeksforgeeks.org/count-pairs-with-given-sum/

Count pairs with given sum

Given an array of integers, and a number ‘sum’, find the number of pairs of integers in the array whose sum is equal to ‘sum’.

Examples:

Input  :  [1, 5, 7, -1],
          sum = 6
Output :  2
Pairs with sum 6 are (1, 5) and (7, -1)

Input  :  [1, 5, 7, -1, 5],
          sum = 6
Output :  3
Pairs with sum 6 are (1, 5), (7, -1) &
                     (1, 5)

Input  :  [1, 1, 1, 1],
          sum = 2
Output :  6
There are 3! pairs with sum 2.

Input  :  [10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1],
          sum = 11
Output :  9
"""


def get_pairs_count(arr, target):
    d = {}

    for num in arr:
        d[num] = d.get(num, 0) + 1

    twice_count = 0

    for num in arr:
        twice_count += d.get(target - num, 0)

        # use arr= [1, 1, 1, 1], target = 2 example to understand this if branch
        if target - num == num:
            twice_count -= 1

    return int(twice_count / 2)


if __name__ == "__main__":
    print(get_pairs_count([1, 5, 7, -1], 6))
