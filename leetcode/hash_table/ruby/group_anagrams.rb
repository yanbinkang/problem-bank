=begin
https://leetcode.com/problems/sort-characters-by-frequency/description/

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"],
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]

Note: All inputs will be in lower-case.

O(n*mlog(m)) in time and O(n) in space, where m represents the average length of the strings in strs and n is the number of the strings in strs
=end
def group_anagrams(strs)
  strs_hash = {}

  strs.each do |str|
    sorted_string = str.chars.sort.join

    strs_hash[sorted_string] = strs_hash.fetch(sorted_string, []) + [str]
  end

  strs_hash.values
end

if __FILE__ == $0
  strs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
  puts group_anagrams(strs).inspect
end
