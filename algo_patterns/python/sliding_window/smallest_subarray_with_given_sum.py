"""
Given an array of positive numbers and a positive number 'S', find the length of the smallest
subarray whose sum is greater than or equal to 'S'. Return 0, if no such subarray exists.

Example 1:
    Input: [2, 1, 5, 2, 3, 2], S=7
    Output: 2
    Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].

Example 2:
    Input: [2, 1, 5, 2, 8], S=7
    Output: 1
    Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].

Example 3:
    Input: [3, 4, 1, 1, 6], S=8
    Output: 3
    Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6]

Note to self: The difference between this problem and Maximum Sum Subarray of Size K: in this problem, the size of the sliding window is not fixed, so we use a while loop to slide the window.
"""

# Time and space complexity O(N), O(1)


def smallest_subarray_with_given_sum(s, arr):
    """
    can also:
    import math
    min_length = math.inf
    """
    min_length, window_start = float('inf'), 0
    window_sum = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        while window_sum >= s:
            min_length = min(window_end - window_start + 1, min_length)
            window_sum -= arr[window_start]
            window_start += 1

    return 0 if min_length == float('inf') else min_length


if __name__ == "__main__":
    print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 3, 2]))
    print(smallest_subarray_with_given_sum(7, [2, 1, 5, 2, 8]))
    print(smallest_subarray_with_given_sum(8, [3, 4, 1, 1, 6]))
    print(smallest_subarray_with_given_sum(8, []))
