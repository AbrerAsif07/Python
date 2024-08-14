# returns true or false
# takes in parameters in/not in
my_lst = [1, 2, 3, 4, 4, 5, 5, 6, 7, 8, 9]
# print(7 in my_lst)
# print(11 in my_lst)
result = []
for num in my_lst:
    if num not in result:
        result.append(num)
print(result)
