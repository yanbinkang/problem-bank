# def remove_white_space(a_string):
#     return ''.join(a_string.split())

def remove_white_space(a_string):
    i = 0
    result_str = ''
    while i < len(a_string):
        if a_string[i] == '\t' or a_string[i] == ' ':
            i += 1
        else:
            result_str += a_string[i]
        i += 1
    return result_str


print remove_white_space('    Quick brown fox jumped over the lazy dog.    ')
