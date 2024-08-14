my_lst = [54, 65, 321, 76876, 432, 65, 78, 54, 3454]
total = 0
n = len(my_lst)
for index in range(0, n):
    if index % 2 != 0:
        total = total + my_lst[index]
print(total)
