# sets -> collection of unique elements
s = {1, 2, 3, 3, 6}
s.add(10)
# print(s)s

empty_set = set()

# print(type(empty_set))


# method
# add, remove, clear, pop,
# unioun -> all numbers in set 1 and 2,
# intersection -> only the common numbers in set 1 and 2

# s.remove(10)
# print(s)

# s.pop()
# print(s)

# s.clear()
# print(s)

# union and intersection
s1 = {2, 1, 5, 9}
s2 = {4, 5, 3, 7, 9}
union = s1.union(s2)
intersection = s1.intersection(s2)
print(union)
print(intersection)
