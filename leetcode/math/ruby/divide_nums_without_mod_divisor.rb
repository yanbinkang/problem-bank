=begin
https://www.geeksforgeeks.org/divide-two-integers-without-using-multiplication-division-mod-operator/

https://www.geeksforgeeks.org/division-without-using-operator/

Given a two integers say a and b. Find the quotient after dividing a by b without using multiplication, division and mod operator.

Example:

Input : a = 10, b = 3
Output : 3

Input : a = 43, b = -8
Output :  -5
=end
def divide(dividend, divisor)
  # sign = dividend < 0 || divisor < 0 ? -1 : 1
  return 0 if dividend.zero?

  return Float::INFINITY if divisor.zero?

  sign = if dividend < 0 && divisor < 0
           1
         elsif dividend < 0 || divisor < 0
           -1
         else
           1
         end

  dividend = dividend.abs
  divisor = divisor.abs
  quotient = 0

  while dividend >= divisor
    dividend -= divisor
    quotient += 1
  end

  sign * quotient
end

if $PROGRAM_NAME == __FILE__
  p divide(10, 3)
  puts
  p divide(43, -8)
  puts
  p divide(-10, -3)
  puts
  p divide(14, -2)
  puts
  p divide(-11, 3)
  puts
  p divide(-11, 0)
  puts
  p divide(0, 3)
  puts
  p divide(0, 0)
end
