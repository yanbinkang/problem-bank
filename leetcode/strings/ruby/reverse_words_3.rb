=begin
https://leetcode.com/problems/reverse-words-in-a-string-iii/#/description

Given a string, you need to reverse the order of characters in each
word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

Note: In the string, each word is separated by single space
and there will not be any extra space in the string.
=end
def reverse_words(s)
  s = s.chars
  index = 0

  (s.length + 1).times do |i|
    if i == s.length || s[i] == ' '
      reverse_char(s, index, i - 1)
      index = i + 1
    end
  end

  s.join
end

def reverse_char(str, first, last)
  while first <= last
    temp = str[first]
    str[first] = str[last]
    str[last] = temp

    first += 1
    last -= 1
  end
end

def reverse_words_1(s)
  result = []
  s.split.each do |word|
    result << word.reverse
  end

  result.join(' ')
end

if $PROGRAM_NAME == __FILE__
  puts reverse_words("Let's take LeetCode contest")
  puts
  puts reverse_words_1("Let's take LeetCode contest")
end
