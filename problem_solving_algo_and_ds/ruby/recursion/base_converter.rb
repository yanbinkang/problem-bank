def base_converter(n, base)
  convert_str = "0123456789ABCDEF"
  if n < base
    return convert_str[n]
  else
    return base_converter(n / base, base) + convert_str[n % base]
  end
end

puts base_converter(8, 2)
