=begin
https://leetcode.com/problems/word-pattern/

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.

https://discuss.leetcode.com/topic/26573/very-fast-3ms-java-solution-using-hashmap

https://leetcode.com/problems/isomorphic-strings/
=end
def word_pattern(pattern, string)
  words = string.split(' ')
  words_length = words.length
  d = {}

  return false if words_length != pattern.size

  words_length.times do |i|
    char = pattern[i]

    if d.key?(char)
      return false if d[char] != words[i]
    else
      # at this point, we know the pattern and word (key/value pair) can be stored dict.
      # But if word is already stored as a value in dict, return false.
      # This means its already been associated with another pattern. See the last example
      return false if d.value?(words[i])

      d[char] = words[i]
    end
  end

  true
end

if $PROGRAM_NAME == __FILE__
  p word_pattern('abba', 'dog cat cat dog')
  p word_pattern('abba', 'dog cat cat fish')
  p word_pattern('abba', 'dog dog dog dog')
end
