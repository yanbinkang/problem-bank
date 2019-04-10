=begin
https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

https://discuss.leetcode.com/topic/44237/java-o-n-solution-bucket-sort

Algorithm:
1) Use hash table to store elements in input array as keys and number of occurances as values

2) Create a temp list with size of length of input array + 1.

3) Iterate through the key, value pair in hash table in step 1. With the value as an index, store the key in the array. If index at value is None (bucket[frequency] is None) initiate an empty array at that index, then finally append key.

4) Create a results array to store final answer.

5) Iterate through the temp array from the back to front (reverse iteration).

6) When the there is a value stored in the index of the temp array, store that value in results array

7) Return results array.
=end
def top_k_frequent(nums, k)
  bucket = [nil] * (nums.length + 1)
  frequency_map = {}

  nums.each do |num|
    frequency_map[num] = frequency_map.fetch(num, 0) + 1
  end

  frequency_map.each do |key, frequency|
    bucket[frequency] = [] if bucket[frequency].nil?

    bucket[frequency] << key
  end

  res = []

  bucket.length.times.reverse_each do |i|
    res += bucket[i] if bucket[i] && res.length < k
  end

  res[0...k]
end

if $PROGRAM_NAME == __FILE__
  puts top_k_frequent([1, 1, 1, 2, 2, 3], 2)
  puts top_k_frequent([3,0,1,0], 1)
  puts top_k_frequent([1], 1)
end
