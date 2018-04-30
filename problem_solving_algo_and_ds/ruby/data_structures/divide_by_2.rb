require_relative 'stack'

def divide_by_2(num)
  stack = Stack.new

  while num > 0
    rem = num % 2
    stack.push(rem)
    num = num / 2
  end

  conv_num = ""

  while !stack.is_empty
    conv_num += stack.pop.to_s
  end

  return conv_num
end

p divide_by_2(12)
