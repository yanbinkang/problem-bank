"""
https://leetcode.com/problems/pascals-triangle-ii/#/description

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?

Soluton:

https://discuss.leetcode.com/topic/2510/here-is-my-brief-o-k-solution

The basic idea is to iteratively update the array from the end to the beginning.

it's O(k) space complexity, not time complexity. The space used is just the k+1 array elements, hence O(k)
"""


def get_row(row_index):
    result = [1] * (row_index + 1)

    # we start from 1 in each iteration because we dont care about index 0 when generating the pascals-triangle. IT'S ALWAYS 1!
    for i in range(1, row_index + 1):
        """
        this here (inner loop) says: we're starting from the end
        If i = 2, we'll start updating from index 1. If i = 3, we'll start updating from index 2 etc. WE DON'T CARE ABOUT THE INDEX i IS ON (when the loop starts) BECAUSE ITS ALWAYS 1!
        """
        for j in reversed(range(1, i)):
            result[j] = result[j - 1] + result[j]

    return result


if __name__ == '__main__':
    print(get_row(3))
