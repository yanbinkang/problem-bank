"""
ref: http://www.geeksforgeeks.org/transform-one-string-to-another-using-minimum-number-of-given-operation/
"""
def can_be_transformed(str_1, str_2):
    return sorted(str_1) == sorted(str_2)

def min_ops(str_a, str_b):
    if can_be_transformed(str_a, str_b):
        res = 0
        n = len(str_a)

        i = n - 1
        j = n - 1

        while i >= 0:
            while i >= 0 and str_a[i] != str_b[j]:
                i -= 1
                res += 1

            if i >= 0:
                i -= 1
                j -= 1

        return res

    return -1

if __name__ == '__main__':
    a = 'EACBD'
    b = 'EABCD'

    print min_ops(a, b)
