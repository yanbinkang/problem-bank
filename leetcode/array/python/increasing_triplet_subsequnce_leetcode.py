"""
https://leetcode.com/problems/increasing-triplet-subsequence/#/description

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 <= i < j < k <= n-1 else return false.

Your algorithm should run in O(n) time complexity and O(1) space complexity.

Examples:
Given [1, 2, 3, 4, 5],
return true.

Given [5, 4, 3, 2, 1],
return false.

ref: https://discuss.leetcode.com/topic/37281/clean-and-short-with-comments-c
ref: https://discuss.leetcode.com/topic/37426/concise-java-solution-with-comments

Algo:

Assign two variables c1, c2 to float('inf').

If the first number we see is less than or equal c1, we've found our min number so far. set c1 to that number. (first else conditional)

Now the next number we want should be greater than c1. So if the next number we see is greater than c1 but less than or euqal to c2, we've found our next number in the triplet. (2nd else conditional)

Finally, we need another number which is greater than c1 and c2. if we find this number, return True.

If we get to the end of the loop without meeting these conditions, we return False.

IMPORTANT: look at this example, [1, 2, 0, 3], isn't this a violation?

Read:

This is the very case that confused me when I first read OPs solution. The logic is rather terse but works for such inputs. In case anyone else is reading and would like a further elaboration:

initial : [1, 2, 0, 3], small = MAX, big = MAX
loop1 : [1, 2, 0, 3], small = 1, big = MAX
loop2 : [1, 2, 0, 3], small = 1, big = 2
loop3 : [1, 2, 0, 3], small = 0, big = 2 // <- Uh oh, 0 technically appeared after 2
loop4 : return true since 3 > small && 3 > big // Isn't this a violation??

If you observe carefully, the moment we updated big from MAX to some other value, that means that there clearly was a value less than it (which would have been assigned to small in the past). What this means is that once you find a value bigger than big, you've implicitly found an increasing triplet.
"""
def increasing_triplet(nums):
    c1, c2 = float('inf'), float('inf')

    for num in nums:
        if num <= c1:
            c1 = num # c1 is min seen so far (it's a candidate for 1st element)
        elif num <= c2: # here when x > c1, i.e. x might be either c2 or c3
            c2 = num
        else: # here when we have/had c1 < c2 already and x > c2
            return True # the increasing subsequence of 3 elements exists

    return False

if __name__ == '__main__':
    print increasing_triplet([1, 2, 3, 4, 5])
    print('\n')
    print increasing_triplet([5, 4, 3, 2, 1])
    print('\n')
    print increasing_triplet([0, 4, 2, 1, 0, -1, -3])
    print('\n')
    print increasing_triplet([1, 2, 0, 3])
