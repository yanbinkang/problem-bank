require_relative 'stack'

def infix_to_postfix(infix_expr)
  prec = {}
  prec["^"] = 4
  prec["*"] = 3
  prec["/"] = 3
  prec["+"] = 2
  prec["-"] = 2
  prec["("] = 1

  stack = Stack.new

  postfix_array = []
  tokens = infix_expr.split

  tokens.each do |token|
    if "ABCDEFGHIJKLMNOPUVWXYZ".include?(token) || "0123456789".include?(token)
      postfix_array << token
    elsif token == "("
      stack.push(token)
    elsif token == ")"
      top_token = stack.pop
      while top_token != "("
        postfix_array << top_token
        top_token = stack.pop
      end
    else
      while (!stack.is_empty) && (prec[stack.peek] >= prec[token])
        postfix_array << stack.pop
      end

      stack.push(token)
    end
  end

  while !stack.is_empty
    postfix_array << stack.pop
  end

  return postfix_array.join(" ")

end

puts infix_to_postfix("( A + B ) * ( C + D )")
puts infix_to_postfix("( A + B ) * C")
puts infix_to_postfix("5 * 3 ^ ( 4 - 2 )")
