=begin
https://leetcode.com/problems/minimum-window-substring/

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.

ref: https://discuss.leetcode.com/topic/30941/here-is-a-10-line-template-that-can-solve-most-substring-problems
=end
def min_window(s, t)
  return '' if t.length > s.length

  d = {}

  t.chars.each do |c|
    d[c] = d.fetch(c, 0) + 1
  end

  left, right, head, count = 0, 0, 0, t.length

  min_length = Float::INFINITY

  while right < s.length
    # If char in s exists in t, decrease counter
    count -= 1 if d.fetch(s[right], 0) > 0

    # Decrease d[s[right]]. If char does not exist in t, d[s[right]] will be negative
    d[s[right]] = d.fetch(s[right], 0) - 1

    right += 1

    while count.zero?
      if right - left < min_length
        min_length = right - left
        head = left
      end

      # if we care about s[left], we need to update its value and count

      # Why? If we care about s[left], we would have decremented the count and value earlier. We need to add it back in case we see another char == s[left]

      # remember earlier we said if the char does not exist in t d[s[right]] will be negative. So in the same vain if d[s[left]] is not greater than zero, we don't care about this char so we won't increment count for the next window!

      if d.include?(s[left])
        d[s[left]] += 1

        count += 1 if d[s[left]] > 0
      end

      left += 1
    end
  end

  return '' if min_length == Float::INFINITY
  return s[head...head + min_length]
end

if __FILE__ == $0
  puts min_window('ADOBECODEBANC', 'ABC') #BANC
  puts min_window('A', 'A') #A
  puts min_window('cabwefgewcwaefgcf', 'cae')  #cwae
  puts min_window('aa', 'aa') #aa
end
