=begin
https://leetcode.com/problems/string-compression/

Given an array of characters, compress it in-place.

The length after compression must always be smaller than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place, return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:

Input:
["a","a","b","b","c","c","c"]

Output:
Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".


Example 2:

Input:
["a"]

Output:
Return 1, and the first 1 characters of the input array should be: ["a"]

Explanation:
Nothing is replaced.

Example 3:

Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

Output:
Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed. "bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.

solution ref: https://leetcode.com/problems/string-compression/discuss/122241/Python-solution-with-detailed-explanation
=end
# @param {Character[]} chars
# @return {Integer}
def compress(chars)
  rptr = 0
  wptr = 0

  while rptr < chars.length
    ch = chars[rptr]
    counter = 0
    while rptr < chars.length && chars[rptr] == ch
      rptr += 1
      counter += 1
    end

    chars[wptr] = ch
    wptr += 1

    next if counter == 1

    counter.to_s.chars.each do |c|
      chars[wptr] = c
      wptr += 1
    end

  end

  wptr
end

if $PROGRAM_NAME == __FILE__
  chars = %w[a b b b b b b b b b b b b]
  puts compress(chars)
end
