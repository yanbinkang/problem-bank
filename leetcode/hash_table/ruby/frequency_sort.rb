=begin
https://leetcode.com/problems/sort-characters-by-frequency/

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.

Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.

similar to: https://leetcode.com/problems/top-k-frequent-elements/

solution: use bucket sort

O(n) time, O(n) space
=end

def frequency_sort(s)
  result = ''

  bucket = [nil] * (s.length + 1)

  hash_map = {}

  s.chars.each do |char|
    hash_map[char] = hash_map.fetch(char, 0) + 1
  end

  hash_map.each do |key, value|
    bucket[value] = [] if bucket[value].nil?

    bucket[value] << key
  end

  (0..bucket.length - 1).reverse_each do |i|
    next if bucket[i].nil?

    bucket[i].each do |char|
      result += char * i
    end
  end

  result
end

if $PROGRAM_NAME == __FILE__
  puts frequency_sort('Aabb')
  puts frequency_sort('tree')
  puts frequency_sort('cccaaa')
end
