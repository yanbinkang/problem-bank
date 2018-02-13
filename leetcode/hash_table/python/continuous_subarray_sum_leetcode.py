"""
https://leetcode.com/problems/continuous-subarray-sum/#/description

Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

similar to:

https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

and

https://leetcode.com/problems/contiguous-array/

O(n) time O(k) space

https://discuss.leetcode.com/topic/80793/java-o-n-time-o-k-space

We iterate through the input array exactly once, keeping track of the running sum mod k of the elements in the process. If we find that a running sum value at index j has been previously seen before in some earlier index i in the array, then we know that the sub-array (i,j] contains a desired sum.

Note to self: NEED TO UNDERSTAND THIS SHIT!
Question to self: DO YOU STILL UNDERSTAND WHY WE'RE SETTING hash_map[0] = -1?
"""
def check_subarray_sum(nums, k):
    hash_map = {}
    hash_map[0] = -1

    running_sum = 0

    for i in range(len(nums)):
        running_sum += nums[i]

        if k != 0:
            running_sum = running_sum % k

        if running_sum in hash_map:
            if i - hash_map[running_sum] > 1:
                return True
        else:
            hash_map[running_sum] = i

    return False



if __name__ == '__main__':
    print check_subarray_sum([23, 2, 4, 6, 7], 6)
    print check_subarray_sum([23, 2, 6, 4, 7], 6)
    print check_subarray_sum([7, 6, 6], 6)
    print check_subarray_sum([0, 0], 0)
    print check_subarray_sum([0], -1)

