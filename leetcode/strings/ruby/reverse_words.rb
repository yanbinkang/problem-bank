=begin
https://leetcode.com/problems/reverse-words-in-a-string/#/description

Given an input string, reverse the string word by word.

For example,

Given s = "the sky is blue",

return "blue is sky the".

Clarification:
    - What constitutes a word?
      A sequence of non-space characters constitutes a word.

    - Could the input string contain leading or trailing spaces?
      Yes. However, your reversed string should not contain leading or trailing spaces.

    - How about multiple spaces between two words?
      Reduce them to a single space in the reversed string.

O(n) time O(n) space

Note: In python str.split() handles whitespcae trimming and runs of consecutive whitespace in the string.
=end
def reverse_words(s)
  s = s.split

  reverse_chars(s, 0, s.length - 1)

  s.join(' ')

  # s.split.reverse.join(' ')
end

def reverse_chars(s, first, last)
  while first <= last
    temp = s[first]
    s[first] = s[last]
    s[last] = temp

    first += 1
    last -= 1
  end
end

if $PROGRAM_NAME == __FILE__
  puts reverse_words('the sky is blue')
end
