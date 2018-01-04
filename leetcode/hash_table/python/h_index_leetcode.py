"""
https://leetcode.com/problems/h-index/

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has index h if h of his/her N papers have at least h citations each, and the other N - h papers have no more than h citations each.


For example, given citations = [3, 0, 6, 1, 5], which means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as the h-index.

https://discuss.leetcode.com/topic/40765/java-bucket-sort-o-n-solution-with-detail-explanation
"""
def h_index(citations):
    n = len(citations)
    buckets = [0 for _ in range(n + 1)]

    for num in citations:
        if num >= n:
            buckets[n] += 1
        else:
            buckets[num] += 1

    count = 0

    for i in reversed(range(len(buckets))):
        count += buckets[i]

        if count >= i:
            return i

    return 0


if __name__ == '__main__':
    print h_index([3, 0, 6, 1, 5]) # 3
    print h_index([25, 8, 5, 3, 3])
    print h_index([10, 8, 5, 4, 3])
    print h_index([11, 15])
    print h_index([0])


