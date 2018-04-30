from hashlib import md5

"""
Search for a substring in a given string, by comparing hash values
of the strings
"""

def search(string, sub):
    string_legnth, sub_length = len(string), len(sub)
    hsub_digest = md5(sub).digest()
    offsets = []

    if string_legnth > sub_length:
        return offsets


    for i in xrange(string_legnth - sub_length + 1):
        if md5(string[i:i + sub_length]).digest() == hsub_digest:
            if string[i:i + sub_length] == sub:
                offsets.append(i)

    return offsets
