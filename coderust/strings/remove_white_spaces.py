# def remove_white_space(a_string):
#     return ''.join(a_string.split())

def remove_white_space(a_string):
    """
    O(n) time and space
    """
    i = 0
    result_str = ''
    while i < len(a_string):
        if a_string[i] == '\t' or a_string[i] == ' ':
            i += 1
        else:
            result_str += a_string[i]
            i += 1
    return result_str


def remove_white_spcae_2(s):
    if not s or len(s) == 0: return
    s = list(s)

    i, result_str = 0, ''

    while i < len(s):
        if s[i] != ' ' and s[i] != '\t':
            result_str += s[i]
            i += 1
        else:
            i += 1

    return ''.join(result_str)

print remove_white_space('    Quick brown fox jumped over the lazy dog.    ')
print '\n'
print remove_white_spcae_2('    Quick brown fox jumped over the lazy dog.    ')
