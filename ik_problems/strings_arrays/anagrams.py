"""
Problem: http://www.lifeincode.net/programming/leetcode-anagrams-java/
"""

def anagrams(a_list):
	my_dict = {}
	result = []

	for word in a_list:
		sorted_word = "".join(sorted(word))

		if sorted_word in my_dict:
			my_dict[sorted_word].append(word)
		else:
			my_dict[sorted_word] = [word]

	for val in my_dict:
		if len(my_dict[val]) > 1:
			result.append(my_dict[val])

	return result

my_list = ["foo", "bar", "aaron", "aanor", "abate", "reset", "eerst"]
print anagrams(my_list)
