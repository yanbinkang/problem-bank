# ref: https://leetcode.com/problems/sum-of-two-integers/discuss/84418/Ruby-Solution

def get_sum(a, b)
  # http://stackoverflow.com/questions/8698959/how-to-force-ruby-to-store-a-small-number-as-32-bit-integer
  a = Array(a).pack('l').unpack('l').first
  b = Array(b).pack('l').unpack('l').first

  return a if b.zero?
  return b if a.zero?

  sum = a ^ b
  carry = (a & b) << 1

  get_sum(sum, carry)

  # [a, b].sum
end

if __FILE__ == $0
  p get_sum(1, -1)
end
