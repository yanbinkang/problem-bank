"""
https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

https://discuss.leetcode.com/topic/44237/java-o-n-solution-bucket-sort

Algorithm:
1) Use hash to store elements in input array as keys and number of occurances as values

2) Create a temp list with size of length of input array + 1.

3) Iterate through the key, value pair in hash in step 1. store the value in the temp array's index with key as value. When index at the temp array is None initiate an empty array at that index. Then finally append num.

4) Create a results array to store final answer

5) Iterate through the temp array from the back to front (reverse iteration).

6) When the there is a value stored in the index of the temp array, store that value in results array

7) Return results array.

Coner case: for a situation where input array is [1,1,1,1,1,1,2,2,2,3,3,3,4,4,4,5] and k = 2 return res[:k]
"""
def top_k_frequent(nums, k):
    bucket = [None for i in range(len(nums) + 1)]
    frequency_map = {}

    for n in nums:
        frequency_map[n] = frequency_map.get(n, 0) + 1

    for key, frequency in frequency_map.items():
        if bucket[frequency] is None:
            bucket[frequency] = []

        bucket[frequency].append(key)

    # print bucket

    res = []

    # pos = len(bucket) - 1
    # while pos >= 0 and len(res) < k:
    #     if bucket[pos] is not None:
    #         res.extend(bucket[pos])

    #     pos -= 1

    for i in reversed(range(len(bucket))):
        if bucket[i] and len(res) < k:
            res.extend(bucket[i])

    return res



if __name__ == '__main__':
    print top_k_frequent([1,1,1,2,2,3], 2)
    print('\n')
    print top_k_frequent([3,0,1,0], 1)
    print('\n')
    print top_k_frequent([1], 1)
    # print('\n')
    # print top_k_frequent([1,1,1,1,1,1,2,2,2,3,3,3,4,4,4,5], 2)
