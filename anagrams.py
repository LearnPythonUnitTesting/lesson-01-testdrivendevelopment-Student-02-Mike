import itertools


def get_anagrams(elements):
    return sorted(set(["".join(perm) for perm in itertools.permutations(elements)]))


def get_number_of_anagrams(elements):
    length = len(get_anagrams(elements))
    return length


# str = 'apple'
# anagrams = getAnagrams(str)
# number = getNumberOfAnagrams(str)
#
# print(anagrams)
# print(number)
