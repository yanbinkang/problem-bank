"""
https://leetcode.com/problems/can-place-flowers/#/description

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False

Note:
    1. The input array won't violate no-adjacent-flowers rule.
    2. The input array size is in the range of [1, 20000].
    3. n is a non-negative integer which won't exceed the input array size.
"""
def can_place_flowers(flowerbed, n):
    flowerbed.insert(0, 0)
    flowerbed.append(0)

    i = 1

    while i < len(flowerbed) - 1:
        if flowerbed[i - 1] + flowerbed[i] + flowerbed[i + 1] == 0:
            n -= 1
            i += 1
        i += 1

    return n <= 0

if __name__ == '__main__':
    print can_place_flowers([1,0,0,0,1], 1)
    print can_place_flowers([1,0,0,0,1], 2)
    print can_place_flowers([1,0,0,0,0,1], 2)
    print can_place_flowers([0,0,1,0,1], 1)
