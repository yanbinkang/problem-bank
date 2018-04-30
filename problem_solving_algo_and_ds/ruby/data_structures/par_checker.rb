require_relative 'stack'

def par_checker(symbol_string)
  if symbol_string.length.odd?
    return false
  end

  stack = Stack.new

  symbol_string.chars.each do |char|
    if char == "("
      stack.push(char)
    else
      if !stack.is_empty
        stack.pop
      end
    end
  end

  if stack.is_empty
    return true
  else
    return false
  end
end

puts par_checker('((()))')
puts par_checker('(()')
