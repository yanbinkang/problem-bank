def rotate_array_in_place(nums, k):
    """
    algorithm:

    let a= [1,2,3,4,5,6,7]
    k = 3.

    1. we have to first reverse the whole array by swapping first element with the last one and so on..
    you will get [7, 6, 5, 4, 3, 2, 1]

    2. reverse the elements from 0 to k - 1
    reverse the elements 7, 6, 5
    you will get [5, 6, 7, 4, 3, 2, 1]

    3. reverse the elements from k to n - 1
    reverse the elements 4,3,2,1
    you will get [5, 6, 7, 1, 2, 3, 4]

    Note: we do k = k % len(nums) because sometimes, k is larger than the length of array. For example nums = [1, 2, 3, 4, 5], k = 12, this means we only need to rotate the last two numbers. k = k % nums.length = 2
    """
    k = k % len(nums)

    reverse(nums, 0, len(nums) - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, len(nums) - 1)

def reverse(nums, first, last):
    while first < last:
        temp = nums[first]
        nums[first] = nums[last]
        nums[last] = temp

        first += 1
        last -= 1
