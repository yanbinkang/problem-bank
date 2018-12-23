=begin
https://leetcode.com/problems/count-and-say

The count-and-say sequence is the sequence of integers beginning as follows:
1, 11, 21, 1211, 111221, ...

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
Given an integer n, generate the nth sequence.

Note: The sequence of integers will be represented as a string.

O(n * m) time where n is the integer given and m is the size of string at step n.

O(m) space where m is the size of the string at step n
=end

# @param {Integer} n
# @return {String}
def count_and_say(n)
  s = '1'

  (1..n - 1).each do |_i|
    string = ''
    count = 1

    (1..s.size).each do |j|
      if j == s.size || s[j] != s[j - 1]
        string += count.to_s + s[j - 1]
        count = 1
      else
        count += 1
      end
    end

    s = string
  end
  s
end

if $PROGRAM_NAME == __FILE__
  puts count_and_say(5)
end
