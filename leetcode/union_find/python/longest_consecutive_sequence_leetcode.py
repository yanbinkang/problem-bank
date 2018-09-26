"""
https://leetcode.com/problems/longest-consecutive-sequence/#/description

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

https://discuss.leetcode.com/topic/15383/simple-o-n-with-explanation-just-walk-each-streak

First turn the input into a set of numbers. That takes O(n) and then we can ask in O(1) whether we have a certain number.

Then go through the numbers. If the number x is the start of a streak (i.e., x-1 is not in the set), then test y = x+1, x+2, x+3, ... and stop at the first number y not in the set. The length of the streak is then simply y-x and we update our global best with that. Since we check each streak only once, this is overall O(n)

Overall complexity: O(n) + O(1) * O(k) + O(n) = O(n)
"""
def longest_consecutive_1(nums):
    nums = set(nums) # O(n)
    best_so_far = 0

    for x in nums: # O(n)
        if x - 1 not in nums: # O(1) average time cos nums is a set!
            y = x + 1
            while y in nums: # O(k) where k is num of times y in nums
                y += 1
            best_so_far = max(best_so_far, y - x) # (n)
    return best_so_far


"""
Algorithm:

1) we don't want to count want duplicates in our final answer so use a set to avoid that before proceeding. i.e nums = set(nums)

2) use a dictionary to store the final answer

3) make a set out of all elements in nums. Remember this will add all the numbers to the DisjointSet's map attribute

4) For each num check if num - 1 is present in DisjointSet's map. If so union (num, num -1)

5) Do same for num + 1

6) Iterate over all the nums and find its parent. Store the parent as key and num as value in dictionary.

7 Return value with with max length

NOte: Consecutive numbers will have one parent
"""
from disjoint_set import *
import collections
def longest_consecutive(nums):
    ds = DisjointSet()

    nums = set(nums)

    dic = collections.defaultdict(list)

    for num in nums:
        ds.make_set(num)

    for num in nums:
        # union consecutive numbers together
        if (num - 1) in nums:
            ds.union(num, num - 1)

        # union consecutive numbers together
        if (num + 1) in nums:
            ds.union(num, num + 1)

    for num in nums:
        set_rep = ds.find_set(num)
        dic[set_rep].append(num)

    count  = 0

    for key in dic:
        count = max(count, len(dic[key]))

    return count

    # return len(max(dic.values(), key=len)) # same as above




if __name__ == '__main__':
    print longest_consecutive([100, 4, 200, 1, 3, 2])
    print longest_consecutive([0, 0])
    print longest_consecutive([2147483646,-2147483647,0,2,2147483644,-2147483645,2147483645])
    print longest_consecutive([-7,-1,3,-9,-4,7,-3,2,4,9,4,-9,8,-7,5,-1,-7])
    print longest_consecutive([1,2,2,2,2,2,2,2,2,-2147483648,-2147483647,-2147483646,2147483647])
    print longest_consecutive([1,3,2,2,5,2,3,7])

