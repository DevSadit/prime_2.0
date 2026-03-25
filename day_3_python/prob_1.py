# given a list of tuples with info (name, subject):
# 1. list all unique course.
# 2. list students enrolled in english
#  3. create dictionary
# #

info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

# 1.

# u_courses = set()
# for tup in info:
#     u_courses.add(tup[1])

# print(u_courses)

# 2.
# for name, course in info:
#     if course == "English":
#         print(name)


# 3.
# dict = {}
# for name, course in info:
#     if dict.get(name) == None:
#         dict.update({name: set()})
#     else:
#         dict[name].add(course)

# print(dict)
