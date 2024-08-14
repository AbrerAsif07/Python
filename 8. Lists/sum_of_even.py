my_lst = [54, 65, 321, 76876, 432, 65, 78, 54, 3454]
n = len(my_lst)
sum = 0
for index in range(0, n):
    if my_lst[index] % 2 == 0:
        sum = sum + my_lst[index]
print(sum)
