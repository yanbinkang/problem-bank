def remove_duplicates(a_string):
    """
    O(n) time O(n) space
    """
    result = ''
    count_dict = {}

    for char in a_string:
        count_dict[char] = True

    for key in count_dict:
        result += str(key)

    return ''.join(sorted(result))

print remove_duplicates('abbabcddbabcdeedbc')
