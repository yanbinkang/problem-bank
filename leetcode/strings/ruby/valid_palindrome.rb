=begin
https://leetcode.com/problems/valid-palindrome/?tab=Description

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
  Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.
=end
def is_palindrome(s)
  l = 0
  r = s.size - 1

  while l < r
    l += 1 while l < r && (s[l] =~ /[[:alnum:]]/).nil?

    r -= 1 while l < r && (s[r] =~ /[[:alnum:]]/).nil?

    return false unless s[l].casecmp(s[r]).zero?

    l += 1
    r -= 1
  end

  true
end

def is_palindrome_2(s)
  l = 0
  r = s.size - 1

  while l < r
    if (s[l] =~ /[[:alnum:]]/).nil?
      l += 1
    elsif (s[r] =~ /[[:alnum:]]/).nil?
      r -= 1
    elsif !s[l].casecmp(s[r]).zero?
      return false
    else
      l += 1
      r -= 1
    end
  end

  true
end

if $PROGRAM_NAME == __FILE__
  p is_palindrome('A man, a plan, a canal: Panama')
  puts
  p is_palindrome('race a car')
  puts
  p is_palindrome_2('A man, a plan, a canal: Panama')
  puts
  p is_palindrome_2('race a car')
end
