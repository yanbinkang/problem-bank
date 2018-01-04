"""
https://leetcode.com/problems/minimum-index-sum-of-two-lists/#/description

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:

Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:

Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

Note:
    1) The length of both lists will be in the range of [1, 1000].

    2) The length of strings in both lists will be in the range of [1, 30].

    3) The index is starting from 0 to the list length minus 1.

    4) No duplicates in both lists.

Algorithm:

1) Save each word in list1 and list2 in the dictionary with word as key and index as value. If word is already in dictionary, add new index to previous index value.

2) Generate a new dictionary by filtering for words which are in both lists.

3) From this new dictionary return the keys whose value is equal to min of all the values in the dictionary.
"""
def find_restaurant(list1, list2):
    d = {}

    for i, word in enumerate(list1):
        d[word] = d.get(word, 0) + i

    for i, word in enumerate(list2):
        d[word] = d.get(word, 0) + i

    dic = {k: v for k, v in d.items() if k in list1 and k in list2}

    return [key for key, value in dic.items() if value == min(dic.values())]

if __name__ == '__main__':
    l1 = ['Shogun', 'Tapioca Express', 'Burger King', 'KFC']
    l2 = ['KFC', 'Shogun', 'Burger King']

    l3 = ['Shogun', 'Tapioca Express', 'Burger King', 'KFC']
    l4 = ['Piatti', 'The Grill at Torrey Pines', 'Hungry Hunter Steakhouse', 'Shogun']

    l5 = ['Shogun','Tapioca Express','Burger King','KFC']
    l6 = ['KFC','Burger King','Tapioca Express','Shogun']

    l7 = ['dixyp','uq','q','KFC']
    l8 = ['yl','fjugc','rlni','dixyp','uq','q','KFC']

    l9 = ['Shogun','Tapioca Express','KFC']
    l10 = ['Tapioca Express','Shogun','KFC']

    print find_restaurant(l1, l2)
    print find_restaurant(l3, l4)

    print find_restaurant(l5, l6)
    print find_restaurant(l7, l8)

    print find_restaurant(l9, l10)
