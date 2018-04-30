# calculate numbers betwen 0 and 100 inclusive. For now only "*", "+", "-" allowed.
def infix_eval(input_string)
  stack = []
  result = []
  prec = {}
  prec["*"] = 3
  prec["+"] = 2
  prec["-"] = 1

  tokens = input_string.gsub(/\D|\d+/)

  tokens.each do |token|
    if (0..100).map(&:to_s).include?(token)
      result.push(token)
    else
      while !(stack.empty?) && (prec[stack[stack.length-1]] >= prec[token]) do
        result.push(stack.pop)
      end
      stack.push(token)
    end
  end

  while !stack.empty? do
    result.push(stack.pop)
  end

  return postfix_eval(result)

end

def postfix_eval(postfix_expr)
  stack = []
  postfix_expr.each do |token|
    if (1..100).map(&:to_s).include?(token)
      stack.push(token.to_i)
    else
      opr_2 = stack.pop
      opr_1 = stack.pop
      res = do_math(opr_1, opr_2, token)
      stack.push(res)
    end
  end

  return stack.pop
end

def do_math(num_1, num_2, opr)
  if opr == "*"
    num_1 * num_2
  else
    num_1 + num_2
  end
end

p infix_eval("22*3+4+5*3+5")
