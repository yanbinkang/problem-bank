# start is staring idex
# end is length of string
def is_palindrome(string, start, end):
    if end <= 1:
        return True
    else:
        return string[start] == string[end-1] and is_palindrome(string[start+1:end-1], start, end-2)



print is_palindrome("radar", 0, 5)
print is_palindrome("aibohphobia", 0, 11)
print is_palindrome("albert", 0, 6)
