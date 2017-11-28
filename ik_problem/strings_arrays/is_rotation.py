"""
http://www.geeksforgeeks.org/a-program-to-check-if-strings-are-rotations-of-each-other-or-not/

Given a string s1 and a string s2, write code to check whether s2 is a rotation of s1 using only one call to strstr routine.

Example: s1 = ABCD and s2 = CDAB returns True and s1 = ABCD and s2 = ACBD returns False
"""
def are_rotations(s1, s2):
    size_1 = len(s1)
    size_2 = len(s2)

    if size_1 != size_2:
        return False

    temp = s1 + s1

    return s2 in temp

print are_rotations("ABCD", "CDAB")
print are_rotations("ABCD", "ACBD")
