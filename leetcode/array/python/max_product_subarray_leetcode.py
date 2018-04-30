"""
https://leetcode.com/problems/maximum-product-subarray/description/

Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.

https://discuss.leetcode.com/topic/4417/possibly-simplest-solution-with-o-n-time-complexity

algo:

This is very similar to the maximum subarray sum problem:
https://leetcode.com/problems/maximum-subarray/#/description

Here you keep two values: the max cumulative product UP TO current element starting from SOMEWHERE in the past, and the minimum cumulative product UP TO current element.

At each new element, you could either add the new element to the exisiting product, or start fresh the product from the current index (wipe out previous results), hence the 2 max() lines.

If we see a negative number, the 'candidate' for max should instead become the previous min product, because a bigger number multiplied by negative becomes smaller, hence the swap
"""
def max_product(nums):
    current_max = current_min = max_so_far = nums[0]

    for i in range(1, len(nums)):

        """
        multiplied by negative number makes big number smaller,
        smaller number bigger.
        so redefine the the extremums by swapping them

        When a negative number is multiplied with another negative number we could potentilally get a bigger postive number.

        When a positive number is multiplied with a negative mumber we get a lower minium value.

        note: extremum means the maximum or minimum value of a function.
        """
        if nums[i] < 0:
            temp = current_max
            current_max = current_min
            current_min = temp
            # current_max, current_min = current_min, current_max

        current_max = max(nums[i], current_max * nums[i])
        current_min = min(nums[i], current_min * nums[i])

        max_so_far = max(max_so_far, current_max)

    return max_so_far

if __name__ == '__main__':
    print max_product([2, 3, -2, 4])
    print max_product([-2, 3, -4])
