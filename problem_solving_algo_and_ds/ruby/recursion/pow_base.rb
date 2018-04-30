def pow(base, exp)
  return 1 if exp <= 0

  return base * pow(base, exp - 1)
end

puts pow(5, 3)
