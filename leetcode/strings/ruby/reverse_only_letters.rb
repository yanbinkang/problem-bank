=begin
https://leetcode.com/problems/reverse-only-letters/

Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.



Example 1:

Input: "ab-cd"
Output: "dc-ba"
Example 2:

Input: "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:

Input: "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"


Note:

S.length <= 100
33 <= S[i].ASCIIcode <= 122
S doesn't contain \ or "

ref -> check if char is letter: https://stackoverflow.com/questions/14551256/ruby-how-to-find-out-if-a-character-is-a-letter-or-a-digit
=end
# @param {String} s
# @return {String}
def reverse_only_letters(s)
  s = s.chars
  left = 0
  right = s.length - 1

  while left < right
    if !letter?(s[left])
      left += 1
    elsif !letter?(s[right])
      right -= 1
    else
      s[left], s[right] = s[right], s[left]
      left += 1
      right -= 1
    end
  end

  s.join
end

def letter?(char)
  char =~ /[[:alpha:]]/
end

if $PROGRAM_NAME == __FILE__
  puts reverse_only_letters('Test1ng-Leet=code-Q!')
  puts reverse_only_letters('Qedo1ct-eeLg=ntse-T!')
end
