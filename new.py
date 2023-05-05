# # var = [1, 2, "Bangladesh", 56.5] 
# # print(var)

# # var.append(8)
# # print(var)

# # var.extend([1, 2, 3])
# # print(var)

# # var.insert(10, "Hi")
# # print(var)

# # var.remove('Hi')
# # print(var)

# # var.pop(2)
# # print(var)

# # var.reverse()
# # print(var)

# # print(len(var))

# # print(max(var))
# # print(min(var))

# # var.clear()
# # print(var)




# # new_list = ["Mahadi", 5, "6", 32, "shakib", 3, 5]
# # lent = len(new_list)

# # for i in range(8):     #0, 1, 2, 3, 
# #     if i % 2 == 0:     
# #         print(new_list[i])



# # var1 = input("This number is: ")

# # print(type(var1))

# # my_list = []
# # for i in range(11):
# #     user = int(input("Please type a int caracter: "))
# #     if user % 2 == 0:
# #         if user % 3 == 0:
# #             my_list.append(user)
# #             new_list = my_list
# # print(my_list)




# # new_list = []

# # for i in range(1, 11):
# #     new_inp = int(input("This is a input: "))
# #     if new_inp%2 == 0:
# #         if new_inp % 3 == 0:
# #             new_list.append(new_inp)
# # print(new_list)
# """
# Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.
# Example


# Print the following:

# 8
# -2
# 15
# Input Format

# The first line contains the first integer, .
# The second line contains the second integer, .

# Constraints



# Output Format

# Print the three lines as explained above.

# Sample Input 0

# 3
# 2
# Sample Output 0

# # 5
# # 1
# # 6
# # """




# # num1 = int(input())
# # num2 = int(input())

# # print(num1+num2)
# # print(num1-num2)
# # print(num1*num2)




# my_list = []

# def my_name(*a):
#     sum = 0
#     for num in a:
#         num%2 == 0:
#             sum+=num
#             my_list.append(sum)
        

# my_name([4, 2, 3, 4, 6])
# print(my_list)

# # new_list = []

# # def new_name(a):
# #     if a%2 == 0:
# #         new_list.append(a)
        

# # new_name([4, 2, 3, 4, 6])
# # print(new_list)



# a = (1, 2, 3, 6, 'Ruhin', 'Rafiul')
# print(a)
# # print(type(a))

# print(a[1])



# x = ("apple", "banana", "cherry")
# v = (2, 3, 7, 8, 9, 4)
# v = list(x)
# v[1] = 'Mango'
# x = tuple(v)
# print(x)

# *a, b, c = x
# print(a)
# print(b)
# print(c)

# a = x+v
# print(a)

# x[1] = 5
# print(x)



# my_tuple = ("banana", "mango", "peyara", "apple", "banana", "cherry", "orange")
# # print(type(my_tuple))
# # print(len(my_tuple))
# # print(my_tuple[-1])
# # print(my_tuple[3:])
# hi = len(my_tuple)
# for i in range(hi):
#     if i%2 != 0:
#         print(my_tuple[i])

# you_tuple = ("banana", "mango", "peyara", "apple", "banana", "cherry", "orange")
# hi, *you, my = you_tuple
# print(hi)
# print(you)
# print(my)
    

my_list = [
    {'name': 'Mehedi', 'year_of_experience':2, 'university_name': "Dhaka university"},
    {'name': 'Mehedi', 'year_of_experience':2, 'university_name': "Dhaka university"},
    {'name': 'Mehedi', 'year_of_experience':2, 'university_name': "Dhaka university"},
    {'name': 'Mehedi', 'year_of_experience':2, 'university_name': "Dhaka university"},
]
for i in my_list:
    print(i['name'])











