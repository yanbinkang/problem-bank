"""
https://leetcode.com/problems/set-mismatch/description/

The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Note:
    * The given array size will in the range [2, 10000].
    * The given array's numbers won't have any order.

"""
def findErrorNums(nums):
    """
    :type nums: List[int]
    :rtype: List[int]

    O(n) time and space
    """
    S = set((range(1, len(nums) + 1)))
    seen, result = set(), []

    missing = S - set(nums)

    for num in nums:
        if num in seen:
            result.append(num)
        else:
            seen.add(num)

    return result + list(missing)

def findErrorNums1(nums):
    d = {}
    missing = dup = None

    for num in nums:
        d[num] = d.get(num, 0) + 1

    for i in range(1, len(nums) + 1):
        if i in d:
            if d[i] == 2:
                dup = i
        else:
            missing = i

    return [dup, missing]

if __name__ == '__main__':
    print findErrorNums([1,2,2,4])
    print findErrorNums1([1,2,2,4])
