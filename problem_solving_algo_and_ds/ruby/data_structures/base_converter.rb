require_relative 'stack'

def base_converter(num, base)
  stack = Stack.new
  digits = "0123456789ABCDEF"

  while num > 0
    rem = num % base
    stack.push(rem)
    num = num / base
  end

  conv_num = ""

  while !stack.is_empty
    conv_num += digits[stack.pop]
  end

  return conv_num

end

p base_converter(34, 8)
