# 1.printing the no of odd nos frm the given list

# my_lst = [4, 8, 6, 5, 3, 12, 1, 3]
# total = 0
# n = len(my_lst)
# for i in range(0, n):
#     if my_lst[i] % 2 != 0:
#         total = total + 1
# print(total)


# 2.Total count of all odd and even nos
# my_lst = [4, 8, 6, 5, 3, 12, 1, 3, 6]
# even = 0
# odd = 0
# n = len(my_lst)
# for i in range(0, n):
#     if my_lst[i] % 2 == 0:
#         even = even + 1
#     else:
#         odd = odd + 1
# print(f"no of even no is {even}")
# print(f"no of even no is {odd}")

# 3.Print prime nos in given list

# my_lst = [4, 8, 6, 5, 3, 12, 1, 7, 6, 2]
# def is_prime(num:int):
#     for i in range(2,num):
#         if num%i==0:
#             return False
#         return True
        
# my_lst=[1,2,3,4,5,6,7,8,9,10,11]
# for num in my_lst:
#     if is_prime(num):
#         print(num, end=" ")

# 5.Print sum and product of all elements in list
# my_lst = [4, 8, 6, 5, 3, 12, 1, 7, 6, 2]
# sum = 0
# product = 1
# n = len(my_lst)
# for i in range(0, n):
#     sum = sum + my_lst[i]
#     product = product * my_lst[i]
# print(sum)
# print(product)

# 6.ALl nos divisible by 5 in reverse order
# my_lst = [5, 8, 10, 15, 2, 4, 95, 34]
# n = len(my_lst)
# for i in range(n - 1, -1, -1):
#     if my_lst[i] % 5 == 0:
#         print(my_lst[i], end=" ")

# 7. Print max no frm given list
# my_lst=[1,2,3,4,5,6,69,8,9,10,11]
# maxi=0
# for num in my_lst:
#     if num>maxi:
#         maxi=num
# print(maxi)