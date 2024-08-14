# my_lst = []         Revresing a list by making a copy
# n = 10
# for i in range(n):
#     x = int(input(f"Enter list element {i+1}= "))
#     my_lst.append(x)
# print(my_lst)
# lst2 = []
# for i in range(n, -1, -1):
#     lst2.append(x)
# print(lst2)

# my_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]   Adding 2nd element frm 1st and 2nd element frm last
# n = len(my_lst)
# sum = 0
# for index in range(1, n - 1):
#     sum = sum + my_lst[index]
# print(sum)
# print(my_lst[1] + my_lst[-2])


# my_lst = []
# n = 10
# for i in range(n):
#     x = int(input(f"Enter list element {i+1}= "))
#     my_lst.append(x)
# print(my_lst)
# my_lst2 = []
# for x in range(n):
#     if x % 2 != 0:
#         my_lst2.append(x)
# print(my_lst2)

# my_list = []
# l = int(input("Enter length of the list = "))
# for i in range(l):
#     num = int(input(f"Enter element {i+1} = "))
#     my_list.append(num)

# result = []
# for num in my_list:
#     if num % 2 != 0:
#         result.append(num)

# print(result)


# my_lst = [1, 1, 1, 3, 4, 1, 6, 6, 7, 8, 9, 9, 6, 12, 6]  for count>3 printing those values
# final = []
# for num in my_lst:
#     if my_lst.count(num) > 3:
#         if num not in final:
#             final.append(num)
# print(final)

from typing import List


def removeNth(lst: list, index: int):
    n = len(lst)
    result = []
    for index in range(n):
        x = list.pop(index)
        if x not in result:
            result.append(x)

    else:
        print("Out of index error")


my_list = [1, 2, 3, 4, 56, 67, 8]
y = removeNth(my_list, 2)
print(y)

# from typing import List


# def addOfList(lst1: List, lst2: List) -> List:
#     n = len(lst1)
#     lst3 = []
#     for index in range(n):
#         total = lst1[index] + lst2[index]
#         lst3.append(total)
#     return lst3


# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 4, 3, 1]


# ans = addOfList(list1, list2)
# print(ans)
