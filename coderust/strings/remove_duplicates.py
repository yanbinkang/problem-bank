def remove_duplicates(a_string):
    result = ''
    count_dict = {}

    for char in a_string:
        count_dict[char] = True

    for key in count_dict:
        result += str(key)

    return ''.join(sorted(result))

print remove_duplicates('abbabcddbabcdeedbc')
