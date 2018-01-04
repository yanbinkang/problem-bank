"""
# string permutation in lexicographically order with repetition of characters in the string

O(n!) time O(n) space (if we're not storing the ouput)
"""
def string_permutation(input):
    count_map = {}

    for char in input:
        count_map[char] = count_map.get(char, 0) + 1

    keys = sorted(count_map)

    string, count = [], []

    for key in keys:
        string.append(key)
        count.append(count_map[key])

    perms = [None for i in range(len(input))]
    result = []

    permute_util(string, count, perms, 0, result)

    return result

def permute_util(string, count, perms, level, result):
    if level == len(perms):
        # or print perms
        result.append(''.join(perms))
        return

    for i in range(len(string)):
        if count[i] == 0:
            continue

        perms[level] = string[i]
        count[i] -= 1
        permute_util(string, count, perms, level + 1, result)
        count[i] += 1

if __name__ == '__main__':
    print string_permutation('abc')
    print string_permutation('aabb')
