=begin
https://leetcode.com/problems/palindrome-permutation/

Given a string, determine if a permutation of the string could form a palindrome.

For example,
"code" -> False, "aab" -> True, "carerac" -> True.

https://discuss.leetcode.com/topic/22057/java-solution-w-set-one-pass-without-counters

The idea is to iterate over string, adding current character to set if set doesn't contain that character, or removing current character from set if set contains it.
When the iteration is finished, just return set.size() == 0 || set.size() == 1.

set.size() == 0 corresponds to the situation when there are even number of any character in the string, and
set.size() == 1 corresponds to the fact that there are even number of any character except one.
=end
require 'set'
def can_permute_palindrome(string)
  return false if string.empty?

  char_set = Set.new

  string.chars.each do |char|
    if char_set.include?(char)
      char_set.delete(char)
    else
      char_set << char
    end
  end

  char_set.size.zero? || char_set.size == 1
end

if $PROGRAM_NAME == __FILE__
  p can_permute_palindrome('aab')
  puts
  p can_permute_palindrome('code')
  puts
  p can_permute_palindrome('carerac')
end
