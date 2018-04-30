"""
https://leetcode.com/problems/find-the-duplicate-number/?tab=Description

Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Note:
You must not modify the array (assume the array is read only).

You must use only constant, O(1) extra space.

Your runtime complexity should be less than O(n2).

There is only one duplicate number in the array, but it could be repeated more than once.

algorithm:
This solution is based on binary search.

At first the search space is numbers between 1 to n. Each time I select a number mid (which is the one in the middle) and count all the numbers equal to or less than mid. Then if the count is more than mid, the search space will be [1:mid] otherwise [mid+1:n]. I do this until search space is only one number.

Let's say n=10 i.e [1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10] and I select mid=5. Then I count all the numbers in the array which are less than equal mid. If the there are more than 5 numbers that are less than 5, then by Pigeonhole Principle (https://en.wikipedia.org/wiki/Pigeonhole_principle) one of them has occurred more than once. So I shrink the search space from [1 10] to [1 5]. Otherwise the duplicate number is in the second half so for the next step the search space would be [6 10]

What is the Pigeonhole Principle: In mathematics, the pigeonhole principle states that if n items are put into m containers, with n > m > 0, then at least one container must contain more than one item

https://discuss.leetcode.com/topic/25580/two-solutions-with-explanation-o-nlog-n-and-o-n-time-o-1-space-without-changing-the-input-array

check out O(n) solution: http://keithschwarz.com/interesting/code/?dir=find-duplicate

O(nlogn) time, O(1) space
"""
def find_duplicate(nums):
    low = 1
    high = len(nums) - 1

    while low < high:
        mid = low + (high - low) // 2
        count = 0

        for num in nums:
            if num <= mid:
                count += 1

        if count <= mid:
            low = mid + 1
        else:
            high = mid

    return low

if __name__ == '__main__':
    print find_duplicate([1, 2, 3, 4, 2])
    print find_duplicate([1, 1, 2, 3, 4, 5, 6, 7, 8, 10])
    print find_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 8, 10])
    print find_duplicate([1, 2, 3, 4, 5, 6, 7, 8, 10, 1])
    print find_duplicate([1, 1, 2])


