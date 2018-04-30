"""
A non-empty zero-indexed array A consisting of N integers is given. A slice of that array is a pair of integers (P, Q) such that O <= P <= Q <= N

Integer P is called the beginning of the slice; integer Q is called the end of the slice. The number Q - P + 1 is called the size of the slice. A slice (P, Q) of array A is called ascending if the corresponding items form a strictly increasing sequnce: A[P] < A[P + 1] < ... < A[Q - 1] < A[Q].

Note that we consider a slice (P, P) consisting of one element to be ascending.

For example, consider array A such that:

    A[0] = 2
    A[1] = 2
    A[2] = 2
    A[3] = 2
    A[4] = 1
    A[5] = 2
    A[6] = -1
    A[7] = 2
    A[8] = 1
    A[9] = 3

Pair (0, 3) is a slice of array A of size 4 that is not ascending.

Pair (2, 2) is a slice of size 1 that is ascending.

Pair (4, 5) is a slice of size 2 that is ascending.

Pair (6, 7) and (8, 9) are other slices of size 2 that are ascending.

There is no slice of array A that is ascending and has size greater than 2.

Write a function:

        def solution(A)

that, given a zero-indexed array consisting of N integers, returns the beginning of any ascending slice of maximal size.

For instance, in the above example the function may return 4, 6, or 8 as explained above.

For the following array A consisting of N = 3 elements:

    A[0] = 30
    A[1] = 20
    A[2] = 10

the function may return 0, 1 or 2, because all the ascending slices of this array have size 1.

Assume that:

    * N is an integer within range [1..150,000]
    * each element of A is an integer within the range [-2**31 .. 2**31 - 1]

Complexity:

    * expected worse-case time complexity is O(N)
    * expected worse-case space complexity is O(N), beyond input storage (not counting the storage required for input arguments).

Elements if input can be modified.
"""

"""
ruby code available here: https://gist.github.com/thephw/c48d9b1714f2f3a5bb9c

read about slice_when: http://blog.honeybadger.io/ruby-enumerable-slicing-before-when-and-after/

def index_of_max_ascending_slice(a)
  slices = a.slice_when{|i,j| i >= j}.to_a
  max_size = slices.map(&:length).max
  start_index = slices[0...slices.find_index{|v| v.length == max_size}].flatten.count
end

java: https://github.com/Himansu-Nayak/jse-examples/blob/master/crackingthecoding/src/main/java/com/corvil/SlicePair.java

algo: start from index 0 to len(A) - 1

If A[i] < A[i + 1] we're looking at an ascending slice. so we have to:
    1. Increment current_size by 1

    2. Check if current_size is greater than max_pair. If so increment max_pair by 1. And set max_pair_start to current_start

Else, we're not looking at an ascending slice. SO we have to:
    1. Reset current_size to 1

    2. set current_start to the next element by doing:

            current_start = i + 1

Finally return max_pair_start
"""
def max_slice_2(A):
    left, right = 0, 0
    max_slice_len = 1
    max_slice_start = 0

    for i in range(1, len(A)):
        if A[i - 1] < A[i]:
            right += 1

            if right - left + 1 > max_slice_len:
                max_slice_len = right - left  + 1
                max_slice_start = left
        else:
            left = right = i


    return max_slice_start

def max_slice(A):
    max_slice = 1
    max_slice_start = 0

    current_size = 1
    current_start = 0

    for i in range(len(A) - 1):
        if A[i] < A[i + 1]:
            current_size += 1

            if current_size > max_slice:
                max_slice += 1
                max_slice_start = current_start
        else:
            current_size = 1
            current_start = i + 1

    return max_slice_start

def max_slice_1(A):
    max_slice_start = 0
    max_slice_length = 1
    current_slice_start = 0

    for i in range(1, len(A)):
        if A[i - 1] >= A[i]:
            current_slice_start = i

        if i - current_slice_start + 1 > max_slice_length:
            max_slice_start = current_slice_start
            max_slice_length = i - current_slice_start + 1

    return max_slice_start



def max_slice_3(A):
    left, right = 0, 0
    max_slice_len, max_slice_start = 1, 0

    for i in range(len(A) - 1):
        if A[i] < A[i + 1]:
            right += 1

            if right - left + 1 > max_slice_len:
                max_slice_len = right - left + 1
                max_slice_start = left
        else:
            left = right = i + 1

    return max_slice_start

if __name__ == '__main__':
    print max_slice([2, 2, 2, 2, 1, 2, -1, 2, 1, 3])
    print max_slice([30, 20, 10])
    print('\n')
    print max_slice_1([2, 2, 2, 2, 1, 2, -1, 2, 1, 3])
    print max_slice_1([30, 20, 10])
    print('\n')
    print max_slice_2([2, 2, 2, 2, 1, 2, -1, 2, 1, 3])
    print max_slice_2([30, 20, 10])
    print('\n')
    print max_slice_3([2, 2, 2, 2, 1, 2, -1, 2, 1, 3])
    print max_slice_3([30, 20, 10])

