from collections import deque
def sliding_windows_max(nums, k):
    result = []

    if k > len(nums): return result

    window = deque()

    # find out max for first window
    for i in range(0, k):
        while window and nums[i] >= nums[window[-1]]:
            window.pop()
        window.append(i)

    result.append(nums[window[0]])

    for i in range(k, len(nums)):
        # remove all numbers that are smaller than current number from tail of list
        while window and nums[i] >= nums[window[-1]]:
            window.pop()

        # remove first number if it doesn't fall in the window anymore
        if window and window[0] < i - k + 1:
            """
            think about i - k + 1 as indices in of the array. for eg if i = 3,
            i - k + 1 will be 3 - 3 + 1 = 1. which means that if the index stored at window[0] is less than this number, it's out of the current window and should be removed!
            """
            window.popleft()

        window.append(i)

        result.append(nums[window[0]])

    # return nums[window[0]]
    return result

print sliding_windows_max([-4, 2, -5, 3, 6], 3)
