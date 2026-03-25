# list -> mutable sequence of values
marks = [10, 20, 30, 50, 80, 100, 40, 60]
# print(marks)
# print(len(marks))
# print(marks[1])

# mutability
marks[2] = 40
# print(marks)


# different type of data

test = ["kola", 2, True]
# print(test)


# slicing of list --> sublist

# print(marks[1:5])


# list methods
# append -> Add the value in last,
# insert -> add the value in specific index,
# sort,
# reverse

marks.append(200)

marks.insert(0, 100)

marks.sort(reverse=True)

marks.reverse()
print(marks)
