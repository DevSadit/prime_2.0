# # 10.
# n = int(input("give a number: "))
# g = int(input("guess the number: "))

# while n != g:
#     if n > g:
#         print("too high..")
#     elif n < g:
#         print("too low..")
# print("correct..")


# 1.
# salary = int(input("provide salary: "))
# if salary < 30000:
#     print("the tax rate is 5%")
# elif salary <= 70000:
#     print("the tax rate is 15%")
# else:
#     print("the tax rate is 25%")


# 2.
# a = int(input("first number: "))
# b = int(input("second number: "))
# counter = a
# while counter <= b:
#     if counter % 2 != 0:
#         print(counter)
#     counter += 1


# 3.


# # def rotate(n):
# #     for i in str(n):
# #         print(i)


# rotate(3222)


# 4.
# def count_num(n):
#     count = 0
#     for i in str(n):
#         count += 1
#     print(count)


# count_num(34567)


# 5.
# def sum(a, b):
#     print(a + b)


# sum(3, 4)


# 6.
# a = int(input("a: "))
# b = int(input("b: "))

# while a <= b:
#     if (a % 3 == 0) and (a % 5 == 0):
#         print(a)
#     a += 1


# 7. Design a program to continuously input a number from user & print if it is positive or negative until the user enters “Quit”.

# while True:
#     num = input("provide the number: ")
#     if num == "quit":
#         break

#     num = int(num)
#     if num > 0:
#         print("positive number")
#     else:
#         print("negative number")


# # 8.
# def calculator(a, b, operation):
#     if operation == "+":
#         print(a + b)
#     elif operation == "-":
#         print(a - b)
#     elif operation == "*":
#         print(a * b)
#     elif operation == "/":
#         print(a / b)
#     else:
#         print("the input is wrong..")


# calculator(10, 2, "/")


# 9.
# def ls_prime(n):
#     is_prime = True
#     if n <= 1:
#         is_prime = False
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 is_prime = False
#                 break
#     return is_prime


# if ls_prime(3) == True:
#     print("prime")
# else:
#     print("not prime")
