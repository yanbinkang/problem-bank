=begin
https://leetcode.com/problems/remove-k-digits/description/

Given a non-negative integer num represented as a string,
remove k digits from the number so that
the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be >= k.
The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2
to form the new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200.
Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number
and it is left with nothing which is 0.

ref: https://leetcode.com/problems/remove-k-digits/discuss/88708/Straightforward-Java-Solution-Using-Stack
=end
def remove_kdigits(num, k)
  len = num.length

  return '0' if k == len

  stack = []
  i = 0

  while i < len
    # whenever meet a digit which is less than the previous digit, discard the previous one
    while k > 0 && !stack.empty? && stack.last > num[i]
      stack.pop
      k -= 1
    end

    stack << num[i]
    i += 1
  end

  # corner case like '1111'
  while k > 0
    stack.pop
    k -= 1
  end

  stack.shift while len > 1 && stack.first == '0'

  stack.join
end

p remove_kdigits('10', 1)
