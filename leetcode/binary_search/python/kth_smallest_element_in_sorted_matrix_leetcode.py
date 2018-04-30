"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.

Note:
    * You may assume k is always valid, 1 <= k <= n^2.

algo: use binary search

The key point for any binary search is to figure out the "Search Space".

For me, I think there are two kind of "Search Space" -- index and range(the range from the smallest number to the biggest number).

Most usually, when the array is sorted in one direction, we can use index as "search space", when the array is unsorted and we are going to find a specific number, we can use "range"

Here are two examples of these two "search space":

    1. index -- https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/ ( the array is sorted)

    2. range -- https://leetcode.com/problems/find-the-duplicate-number/ (Unsorted Array)

The reason why we did not use index as "search space" for this problem is the matrix is sorted in two directions, we can not find a linear way to map the number and its index.

let lo and hi represent smallest and largest number resp. in the matrix.

for each row in the matrix, count the number of elements which are smaller than the mid element. Use binary search to find the solution.


Question:

    * you return "left" in the last line. But how do u know the "left" is a value in the matrix?

Answer:

    * Because the loop invariant is left <= Solution <= right. The moment it quits the loop, we also know another condition is true: left >= right.

left <= Solution <= right and left >= right means left == Solution == right.

Think about it, left >= right could mean left == right hence:

        left == Solution == right

Question:

    * Does it matter if we return lo or hi? Return either pass the tests. Just wondering if there is difference between return lo and return hi? And if there is, what would be the test case that return hi failed? Thanks

Answer:

    * There is no difference between return lo and hi here. The reason is quite simple : my loop invariant is [lo, hi), which means when lo = hi, the loop ends

TIme complexity: O(n * logm).

It's doing binary search on the range of the values, and for each value it counts the numbers which are less than the value chosen. The count takes O(n), and it loops logM times where M is the range of values

ref: https://discuss.leetcode.com/topic/52948/share-my-thoughts-and-clean-java-code

ref: https://discuss.leetcode.com/topic/52865/my-solution-using-binary-search-in-c

READ ALL Q & A IN LINKS!
"""

def kthSmallest(matrix, k):
    lo = matrix[0][0]
    hi = matrix[-1][-1]

    while lo < hi:
        mid = (lo + hi) / 2
        count = 0
        j = len(matrix[0]) # allows us to traverse each row

        # we want to count the number of elements smaller than mid in matrix
        for row in matrix:
            # counts the number of elements less than mid in each row
            while j >= 1 and row[j - 1] > mid:
                j -= 1

            count += j

        # we haven't found the required number of elements. look in upper half
        if count < k:
            lo = mid + 1
        else: # look in lower half
            hi = mid
    return lo # return hi


# use quickselect. Average o(n ^ 2) time. O(n) space
def kthSmallest_1(matrix, k):
    result = []

    if not matrix: return result

    for row in matrix:
        result += row

    return quick_select(result, 0, len(result) - 1, k - 1)

def quick_select(result, first, last, k):
    if first == last:
        return result[k]

    split_point = partition(result, first, last)

    if k == split_point:
        return result[k]
    elif k < split_point:
        return quick_select(result, first, split_point - 1, k)
    else:
        return quick_select(result, split_point + 1, last, k)


def partition(self, result, first, last):
    pivot_value = result[first]
    left_mark = first + 1
    right_mark = last
    done = False

    while not done:
        while left_mark <= right_mark and result[left_mark] <= pivot_value:
            left_mark += 1

        while right_mark >= left_mark and result[right_mark] >= pivot_value:
            right_mark -= 1

        if right_mark < left_mark:
            done = True
        else:
            temp = result[left_mark]
            result[left_mark] = result[right_mark]
            result[right_mark] = temp

    temp = result[first]
    result[first] = result[right_mark]
    result[right_mark] = temp
    return right_mark



if __name__ == '__main__':
    matrix = [
               [ 1,  5,  9],
               [10, 11, 13],
               [12, 13, 15]
            ]
    k = 8

    matrix2 = [
                [1, 25, 50],
                [2, 50, 75],
                [3, 75, 100]
              ]
    print kthSmallest(matrix, k)
    print kthSmallest(matrix2, 4)
