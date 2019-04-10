=begin
https://leetcode.com/problems/valid-anagram/description/

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
=end
def is_anagram1(s, t)
  s.chars.sort == t.chars.sort
end

def is_anagram2(s, t)
  h1, h2 = {}, {}

  s.each_char do |char|
    h1[char] = h1.fetch(char, 0) + 1
  end

  t.each_char do |char|
    h2[char] = h2.fetch(char, 0) + 1
  end

  h1 == h2
end

def is_anagram3(s, t)
  dic1, dic2 = [0] * 26, [0] * 26

  s.each_byte do |byte|
    dic1[byte - 'a'.ord] += 1
  end

  t.each_byte do |byte|
    dic2[byte - 'a'.ord] += 1
  end

  dic1 == dic2
end

if $PROGRAM_NAME == __FILE__
  p is_anagram1('anagram', 'nagaram')
  p is_anagram2('rat', 'car')
  puts
  p is_anagram2('anagram', 'nagaram')
  p is_anagram2('rat', 'car')
  puts
  p is_anagram3('anagram', 'nagaram')
  p is_anagram3('rat', 'car')
end
