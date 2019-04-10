=begin
https://leetcode.com/problems/valid-palindrome-ii/description/

Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

O(n) time O(1) space
"""
# ref: https://discuss.leetcode.com/topic/103910/consice-java-solution
"""
algo: Follow normal way (two pointers) to check if s is palindrome. When two chars are not equal, try to skip (pseudo delete) either left one or right one and continue checking.
=end
def valid_palindrome(s)
  return true if s.empty?

  i = 0
  j = s.size - 1

  while i < j
    if s[i] == s[j]
      i += 1
      j -= 1
    elsif pal?(s[0...i] + s[i + 1...s.size]) || pal?(s[0...j] + s[j + 1...s.size])
      return true
    else
      return false
    end
  end

  true
end

def pal?(string)
  l = 0
  r = string.size - 1

  while l < r
    return false if string[l] != string[r]

    l += 1
    r -= 1
  end

  true
end

if $PROGRAM_NAME == __FILE__
  p valid_palindrome('aba')
  puts
  p valid_palindrome('abca')
end