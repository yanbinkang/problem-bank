def is_palindrome(my_string):
    new_str = "".join(i.lower() for i in my_string if i not in [" ", "-", ".", ":", ";", ",", "'"])
    if len(new_str) <= 1:
        return True
    elif is_palindrome(new_str[1:-1]) and new_str[0] == new_str[-1]:
        return True
    else:
        return False

print(is_palindrome("Go hang a salami; I'm a lasagna hog"))
