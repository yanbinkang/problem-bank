"""
There are  students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature, i.e., if  is friend of  and  is friend of , then  is also friend of . A friend circle is a group of students who are directly or indirectly friends.

You are given a   which consists of characters Y or N. If M[i][j] = Y, then ith and jth students are friends with each other, otherwise not. You have to print the total number of friend circles in the class.
"""
from disjoint_set import *
# import collections
def friend_circles_disjoint_set(matrix):
    ds = DisjointSet()
    n = len(matrix)
    # dic = collections.defaultdict(list)
    dic = {}

    for i in range(n):
        ds.make_set(i)

    for i in range(n):
        for j in range(n):
            if i != j and matrix[i][j] == 'Y':
                ds.union(i, j)

    for i in range(n):
        set_rep = ds.find_set(i)
        # dic[set_rep].append(i)
        dic[set_rep] = dic.get(set_rep, []) + [i]

    return len(dic.keys())

if __name__ == '__main__':
    matrix1 = [['Y', 'Y', 'N', 'N'],
              ['Y', 'Y', 'Y', 'N'],
              ['N', 'Y', 'Y', 'N'],
              ['N', 'N', 'N', 'Y']]

    matrix2 = [['Y', 'N', 'N', 'N', 'N'],
             ['N', 'Y', 'N', 'N', 'N'],
             ['N', 'N', 'Y', 'N', 'N'],
             ['N', 'N', 'N', 'Y', 'N'],
             ['N', 'N', 'N', 'N', 'Y']]

    matrix3 =  [['Y', 'N', 'N', 'N', 'N', 'N', 'Y', 'N', 'N', 'N'],
                ['N', 'Y', 'N', 'N', 'N', 'Y', 'N', 'N', 'N', 'Y'],
                ['N', 'N', 'Y', 'N', 'Y', 'N', 'N', 'N', 'N', 'N'],
                ['N', 'N', 'N', 'Y', 'N', 'N', 'N', 'N', 'N', 'N'],
                ['N', 'N', 'Y', 'N', 'Y', 'N', 'N', 'N', 'N', 'N'],
                ['N', 'Y', 'N', 'N', 'N', 'Y', 'N', 'N', 'N', 'N'],
                ['Y', 'N', 'N', 'N', 'N', 'N', 'Y', 'N', 'N', 'N'],
                ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'Y', 'N', 'N'],
                ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'Y', 'N'],
                ['N', 'Y', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'Y']]


    print friend_circles_disjoint_set(matrix1)
    print('\n')
    print friend_circles_disjoint_set(matrix2)
    print('\n')
    print friend_circles_disjoint_set(matrix3)




