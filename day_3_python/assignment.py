# # 1.
# text = input("Enter a string: ")

# if text == text[::-1]:
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")

# # 2.
# nums = [10, 20]
# count = 0
# for i in nums:
#     count += i

# print(count)

# 3.
# list1 = list(map(int, input("Enter first list elements: ").split()))
# list2 = list(map(int, input("Enter second list elements: ").split()))

# print("List 1:", list1)
# print("List 2:", list2)

# merged = list1 + list2


# merged.sort()
# print(merged)


# 4.
# t = (1, 3, 5, 3, 8, 5, 6, 4)
# even = ()
# odd = ()
# for i in t:
#     if i % 2 == 0:
#         even = even + (i,)
#     else:
#         odd = odd + (i,)

# print(even)
# print(odd)


# 6.
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# word_len = {}

# for word in words:
#     word_len[word] = len(word)

# print(word_len)
# print(type(word_len))


# 7.

# txt = input("provide a text: ")
# blank = " "
# count = 0

# for t in txt:
#     if t == blank:
#         count += 1

# print(f"there are {count} spaces.")


# 8

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]

# s1 = set(l1)
# s2 = set(l2)

# # print(s1, s2)

# intersection = s1.intersection(s2)
# # print(intersection)


# if len(intersection) == 0:
#     print("The lists share no common elements.")
# else:
#     print("The lists share common elements:", intersection)


# 9
# numbers = [1, 2, 3, 2, 4, 5, 1, 6, 3]

# repeated = set()

# for item in numbers:
#     if numbers.count(item) > 1:
#         repeated.add(item)

# print("Repeated elements are:", repeated)


# 10
# text = input("Enter a string: ")

# unique_chars = set(text)

# print("Unique characters are:", unique_chars)
# print("Count of unique characters:", len(unique_chars))
