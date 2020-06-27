import itertools


def getAnagrams(elements):
    return sorted(set(["".join(perm) for perm in itertools.permutations(elements)]))


def getNumberOfAnagrams(elements):
    length = len(getAnagrams(elements))
    return length


# str = 'apple'
# anagrams = getAnagrams(str)
# number = getNumberOfAnagrams(str)
#
# print(anagrams)
# print(number)
