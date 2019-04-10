# https://leetcode.com/problems/find-all-anagrams-in-a-string/

# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

# Example 1:

# Input:
# s: "cbaebabacd" p: "abc"

# Output:
# [0, 6]

# Explanation:
# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

# https://discuss.leetcode.com/topic/64434/shortest-concise-java-o-n-sliding-window-solution/4

# loot at this: http://bookshadow.com/weblog/2016/10/23/leetcode-find-all-anagrams-in-a-string/

# https://discuss.leetcode.com/topic/68976/sliding-window-algorithm-template-to-solve-all-the-leetcode-substring-search-problem

def find_anagrams(s, p)
  results = []

  return results if p.length > s.length

  d = {}

  p.chars.each do |char|
    d[char] = d.fetch(char, 0) + 1
  end

  count = p.length

  left, right = 0, 0

  while right < s.length
    if d.include?(s[right])
      count -= 1 if d[s[right]] > 0

      d[s[right]] -= 1
    end

    right += 1

    while count == 0
      if d.include?(s[left] )
        d[s[left]] += 1

        count += 1 if d[s[left]] > 0
      end

      results << left if right - left == p.length

      left += 1
    end
  end

  results
end

if $PROGRAM_NAME == __FILE__
  puts find_anagrams('cbaebabacd', 'abc').inspect
  p find_anagrams('abab', 'ab')
  p find_anagrams('aa', 'bb')
  p find_anagrams('baa', 'aa')
end
