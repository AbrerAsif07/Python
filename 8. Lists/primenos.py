# my_lst = [45, 31, 7, 5, 3, 100, 17, 19, 26, 65, 92]
# n = len(my_lst)
# for index in range(0, n):
#     if my_lst[index] % index == 0:
#         print(my_lst[index])

my_lst = [4, 8, 6, 5, 3, 12, 1, 3]
total = 0
n = len(my_lst)
for i in range(0, n):
    if my_lst[i] % 2 != 0:
        total = total + 1
print(total)
