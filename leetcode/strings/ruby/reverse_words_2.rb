=begin
https://leetcode.com/problems/reverse-words-in-a-string-ii/#/description

Given an input string, reverse the string word by word. A word is
defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the
words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".

Could you do it in-place without allocating extra space?

algorithm: First reverse the whole string, then reverse each word.

O(n) time O(1) space

https://discuss.leetcode.com/topic/8366/my-java-solution-with-explanation

algo:
    1) reverse the whole sentence

    2) then reverse the individual words in the sentence

DO YOU UNDERSTAND WHY WE HAVE TO DO:
    (s.length + 1).times do |i|
      ...
      ...
    end

Because we have to reverse the last word in the sentence, we need to
go to the actual length of the sentence so we can reverse by using:
    reverse_char(s, index, i - 1) where i is the length of the input
=end
def reverse_words(s)
  reverse_chars(s, 0, s.length - 1)

  index = 0

  (s.length + 1).times do |i|
    if i == s.length || s[i] == ' '
      reverse_chars(s, index, i - 1)
      index = i + 1
    end
  end
end

def reverse_chars(str, first, last)
  while first <= last
    temp = str[first]
    str[first] = str[last]
    str[last] = temp

    first += 1
    last -= 1
  end
end

if $PROGRAM_NAME == __FILE__
  s = ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']
  puts "string before revers is: #{s.join}"
  reverse_words(s)
  puts "string after reverse is: #{s.join}"
end
