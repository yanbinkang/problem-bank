"""
http://www.geeksforgeeks.org/median-of-two-sorted-arrays/
http://www.drdobbs.com/parallel/finding-the-median-of-two-sorted-arrays/240169222
https://www.youtube.com/watch?v=_H50Ir-Tves

solution (comparing medians):
1) let m1 be median of first array
2) let m2 be median of second array
3) if m1 == m2 then either m1 or m2 is the median of two arrays
4) if m1 < m2 it means median lies in arr1[m1_idx+1:] and arr2[:m2_idx].
recursively call solve the problem with these arrays as input.
5) if m1 > m2 median lies in arr1[:m1_idx] and arr2[m2_idx+1:]
"""
def get_median(a, b):
    n = len(a)

    if n <= 0:
        return -1

    if n == 1:
        return (a[0] + b[0]) // 2

    if n == 2:
        return (max(a[0], b[0]) + min(a[1], b[1])) // 2

    m1 = median(a)
    m2 = median(b)

    if m1 < m2:
        return get_median(a[a.index(m1):], b[:b.index(m2)+1])
    else:
        return get_median(a[a.index(m1)+1], b[b.index(m2):])

def median(a_list):
    n = len(a_list)
    return a_list[(n-1)/2]


if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = [0, 5, 6, 9]

    print get_median(a, b)
