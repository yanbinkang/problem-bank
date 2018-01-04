"""
solution: http://www.lifeincode.net/programming/leetcode-anagrams-java/
"""
def group_anagrams(strings):
    hash_map = {}
    for string in strings:
        sorted_string = "".join(sorted(string))
        # print sorted_string
        if sorted_string in hash_map:
            hash_map[sorted_string].append(string)
        else:
            hash_map[sorted_string] = [string]

    res = []

    for k, v in hash_map.items():
        if len(v) > 1:
            res.extend(v)

    return res

strings = ['reset', 'steer', 'trees']

print group_anagrams(strings)
