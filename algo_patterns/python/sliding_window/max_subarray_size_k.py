"""
Given an array of positive numbers and a positive number 'k', find the maximum sum of any subarray of size 'k'.

Example 1:
    Input: [2, 1, 5, 1, 3, 2], k=3
    Output: 9
    Explanation: Subarray with maximum sum is [5, 1, 3].

Example 2:
    Input: [2, 3, 4, 1, 5], k=2
    Output: 7
    Explanation: Subarray with maximum sum is [3, 4].
"""
# Brute force O(N * K)


def max_subarray_size_k(k, arr):
    max_sum = 0
    window_sum = 0

    for i in range(len(arr) - k + 1):
        window_sum = 0
        for j in range(i, i + k):
            window_sum += arr[j]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Optimal solution


def max_sub_array_of_size_k(k, arr):
    max_sum = -float('inf')
    window_start, window_total = 0, 0

    for window_end in range(len(arr)):
        window_total += arr[window_end]

        if window_end >= k - 1:
            max_sum = max(window_total, max_sum)
            window_total -= arr[window_start]
            window_start += 1

    return max_sum


if if __name__ == "__main__":
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(3, [2, 1, 5, 1, 3, 2])))
    print("Maximum sum of a subarray of size K: " +
          str(max_sub_array_of_size_k(2, [2, 3, 4, 1, 5])))
