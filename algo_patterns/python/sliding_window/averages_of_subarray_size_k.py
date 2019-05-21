"""
Given an array, find the averages of all subarray of size 'K' in it.

Example:
[1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

Output: [2.2, 2.8, 2.4, 3.6, 2.8]
"""
# Brute force O(N * K) where N is the number of elements in the input array


def find_averages_of_subarrays(k, arr):
    result = []

    for i in range(len(arr) - k + 1):
        _sum = 0.0
        for j in range(i, i + k):
            _sum += arr[j]
        result.append(_sum / k)  # calculate average

    return result

# O(n)


def averages_of_subarrays(k, arr):
    result = []

    window_sum, window_start = 0.0, 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]

        if window_end >= k - 1:
            result.append(window_sum / k)  # calculate average
            window_sum -= arr[window_start]  # subtract the element going out
            window_start += 1  # slide the window ahead

    return result


if __name__ == "__main__":
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))

    print(averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]))
