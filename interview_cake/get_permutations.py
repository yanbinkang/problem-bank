def get_permutations(string):
    if len(string) <= 1:
        return [string]

    all_chars_except_last = string[:-1]
    last_char = string[-1]

    perm_of_chars_except_last = get_permutations(all_chars_except_last)

    possible_pos_to_put_last_char = range(len(all_chars_except_last)+1)
    permutations = []

    for possible_chars in perm_of_chars_except_last:
        for pos in possible_pos_to_put_last_char:
            perm = possible_chars[:pos] + last_char + possible_chars[pos:]
            permutations.append(perm)

    return permutations

print get_permutations("cat")
