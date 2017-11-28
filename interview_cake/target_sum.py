# Given an array of unsorted numbers, determine of any
# two numbers can equal the target sum given.
def target_sum(numbers, target_sum):
    if len(numbers) <= 1:
        return False

    sorted_numbers = sorted(numbers)
    first = 0
    last = len(numbers) - 1

    while first < last:
        current_sum = sorted_numbers[first] + sorted_numbers[last]
        if current_sum == target_sum:
            return True
        elif current_sum > target_sum:
            last -= 1
        else:
            first += 1
    return False

print target_sum([9, 5, 2, 7], 10)
print target_sum([2, 3, 6, 5, 9], 7)
print target_sum([2], 7)
print target_sum([2, 3, 6, 5, 9], 7)
