=begin
https://leetcode.com/problems/group-shifted-strings/

Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:

"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
A solution is:

[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

O(n^2) time O(n) space

algorithm:
  for each string calculate the distance between the consecutive strings. store the distance as key and the string as value. In the end all string that have the same relative distance will be grouped together. Fianlly return the dictionary values.

https://discuss.leetcode.com/topic/71031/python-group-them-by-relative-distance
=end
def group_strings(strings)
  d = Hash.new { |hash, key| hash[key] = []}

  strings.each do |s|
    temp = ''

    (1..s.length - 1).each do |i|
      temp += ( (s[i].ord - s[i - 1].ord) % 26 ).to_s
    end

    d[temp] << s
  end

  d.values
end

if __FILE__ == $0
  puts group_strings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]).inspect
end
