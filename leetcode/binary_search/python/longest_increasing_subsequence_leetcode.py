"""
https://leetcode.com/problems/longest-increasing-subsequence/#/description

Given an unsorted array of integers, find the length of longest increasing subsequence.

WHAT IS A SUBSEQUNCE: A SUBSEQUNCE IS A SEQUENCE IN AN ARRAY WHICH MIGHT NOT BE CONTIGUOUS

For example,

Given [10, 9, 2, 5, 3, 7, 101, 18],

The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n^2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?

solution:

This solution can be viewed as d.p., but I find it easier not to think of it that way.

Runtime: To get an O(n log n ) runtime, I'm going to create a second list S. (Stick with me for now -- I'll get rid of it in a minute to get O(1) space.) I'll do a single pass through nums, and as I look at each element:

    - The length of S will be equal to the length of the longest subsequence I've found to that point.

    - The last element of S will be the last element of that subsequence. (However, the earlier elements may no longer be part of that sequence -- S is not actually the subsequence itself.)

At the end, the length of S will be our solution.

S will be sorted at all times. Each new element is inserted into S, replacing the smallest element in S that is not smaller than it [or the first element which is larger than it] (which we can find with a binary search). If that element is larger than the last element of S, then we extend S by one -- maintaining both properties.

For example, if

    nums = [5, 6, 7, 1, 2, 8, 3, 4, 0, 5, 9]

then after we prcoess the 7:

    S = [5,6,7]

after we process the 2:

    S = [1,2,7]

after we process the 8:

    S = [1,2,7,8]

Then we process the 3:

    S = [1,2,3,8]

We process the 4:

    S = [1,2,3,4]

and now the next three elements:

    S = [0,2,3,4,5,9]

S is not the actual subsequence, but it is the right length (and ends in the right number).

Time: We are making 1 pass on n elements, and doing a binary search each time. So O(n log n) time.

Space: Assuming we are allowed to destroy the list, we don't need S. Since S will never be larger then the number of elements we have looked at, and we only need to look at each element once, we can just use the beginning of nums for S (keeping track of the size of "S" in a separate variable).
"""
def length_of_LIS(nums):
    tails = [0] * len(nums)

    size = 0

    for num in nums:


        """
        Or find the first element in tails that is greater than num
        REMEMBER TAILS WILL ALWAYS BE SORTED!
        """
        first, last = 0, size
        while first < last:
            mid = (first + last) / 2

            """
            if the num is greater than tails[mid], it belongs to the upper half of the array hence: first = mid + 1
            Else, it belongs to the lower half of the array hence: last = mid

            Why not last = mid - 1? Because if the number is not greater than tails[mid], it could be equal to tails[mid]. This caters for that edge case!
            """
            if tails[mid] < num:
                first = mid + 1
            else:
                last = mid

        tails[first] = num
        size = max(first + 1, size)

    return size

# O(n ^ 2) time, O(n) space
"""
Initialize LIS value. Use two pointers i and j

i = 1; j = 0

while i < len(nums):
    while j < j:
        # find LIS

-----------------------------------------------------------
iterator  | j   |  i   |    |     |     |     |     |     |
-----------------------------------------------------------
arr       | 10  |  22  | 9  | 33  | 21  | 50  | 41  | 60  |
-----------------------------------------------------------
LIS       |  1  |  1   | 1  | 1   | 1   |  1  |  1  | 1   |
-----------------------------------------------------------

For each index i, we calculate the length of longest increasing subsequence ending at index i

if arr[i] > arr[j] then we have an increasing subsequence, so LIS[i] becomes max(LIS[i], LIS[j] + 1). That is, if LIS[i] is greater than LIS[j] + 1, do nothing, else change LIS[i]

Note that for LIS[i] where i = 0, LIS[0] is already 1, there is nothing to do, so we initialize i with 1.

Do this till i gets to the end of arr. Finally return the max element in LIS

watch: https://www.youtube.com/watch?v=Ns4LCeeOFS4&index=5&list=PLqM7alHXFySGbXhWx7sBJEwY2DnhDjmxm

"""
def length_of_LIS_DP(nums):
    LIS = [1] * len(nums)
    i_max = 0

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                LIS[i] = max(LIS[i], LIS[j] + 1)

    # cannot return max(LIS) because if nums = [], we'll have a problem
    # ValueError: max() arg is an empty sequence
    for num in LIS:
        if num > i_max:
            i_max = num

    return i_max

if __name__ == '__main__':
    print length_of_LIS([5, 6, 7, 1, 2, 8, 3, 4, 0, 5, 9])
    print length_of_LIS([4, 5, 6, 3])
    print length_of_LIS([10, 9, 2, 5, 3, 7, 101, 18])
    print length_of_LIS([10,9,2,5,3,7,101,18])
    print length_of_LIS([3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10])
    print length_of_LIS([3, 4, -1, 0, 6, 2, 3])
    print('\n')
    print length_of_LIS_DP([5, 6, 7, 1, 2, 8, 3, 4, 0, 5, 9])
    print length_of_LIS_DP([4, 5, 6, 3])
    print length_of_LIS_DP([10, 9, 2, 5, 3, 7, 101, 18])
    print length_of_LIS_DP([10,9,2,5,3,7,101,18])
    print length_of_LIS_DP([3, 4, -1, 5, 8, 2, 3, 12, 7, 9, 10])
    print length_of_LIS_DP([3, 4, -1, 0, 6, 2, 3])
