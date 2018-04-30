"""
You would like to set a password for an email account. However, there are two restrictions on the format of the passowrd. It has to contain at least one uppercase character and it cannot contain any digits.

You are given a string S consisting of N alphanumerical characters. You would like to find the longest substring of S that is a valid password. A substring is defined as a contiguous segment of a string.

For example, given "a0Ba", the substrings that are valid passowrds are "B" and "Ba". Note that "aBa" is not a substring and 'a0B' is not a valid password.

Write a function that givne a non-empty string S consisting of N characters, returns the length of the longest substring that is a valid password. If there is not such substring, your function should return -1.

Example 1:
S = "a0Ba"

return 2

Example 2:
S = "a0bb"

return -1

Assume that:

    - N is an integer within range [1..200];
    - string S consists only of alphanumerical characters (a-z and/or A-Z and/or 0-9)

ref: https://stackoverflow.com/questions/39388558/java-find-the-longest-substring-without-any-number-and-at-least-one-upper-case
"""
def valid_password(s):
    # uncomment lines to print the valid password
    left, right, max_length = 0, 0, 0

    # longest_start, longest_end = 0, 0


    while right < len(s):
        while right < len(s) and s[right].isdigit():
            right += 1

        left = right

        found_upper = False

        while right < len(s) and not s[right].isdigit():
            if s[right].isupper():
                found_upper = True

            right += 1

        # if found_upper and right - left > longest_end - longest_start:
        #     longest_start = left
        #     longest_end = right


        if found_upper:
            max_length = max(max_length, right - left)

    # return s[longest_start: longest_start + longest_end]
    return -1 if max_length == 0 else max_length


if __name__ == '__main__':
    print valid_password('A1abc')       # 1
    print valid_password('a0Ba')        # 2
    print valid_password('abcD123BCV')  # 4
    print valid_password('XYZzb02abc')  # 5
    print valid_password('123BBCvcb')   # 6
    print valid_password('456ABC')      # 3
    print valid_password('a0bb')        # -1


"""
Ruby code

def solution(s)
  valid = s.scan(/([^0-9]*[A-Z]+[a-z]*)/)

  value = valid.flatten

  value.max {|x, y| x.length <=> y.length }

  result = value

  result.empty? ? -1 : result.first.length

end
"""
