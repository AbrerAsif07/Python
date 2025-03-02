"""
1 2 3 
4 5 6
7 8 9
"""

list2D = [
    [1, 2, 3],  # totsl 3 lists nested inside a single list. indexing from 0,1,2
    [4, 5, 6],
    [7, 8, 9],
]
print(f"no of elements= {list2D[2][2]}")
# To print all elements in an array
# i pointer for outer loop and j for inner loop
for i in range(0, 3):  # determines no of rows
    for j in range(0, 3):  # determines no of columns
        print(list2D[i][j])

# print total sum
total = 0
for i in range(0, 3):
    for j in range(0, 3):
        total += list2D[i][j]
print(f"total={total}")

# printing each row value


for i in range(0, 3):
    total = 0
    for j in range(0, 3):
        total += list2D[i][j]
    print(f"total of each row wise = {total}")

    # To print Diagonal elements
for i in range(0, 3):
    for j in range(0, 3):
        if i == j:
            print(f"Diagonal elements  = {list2D[i][j]}")

# To print left diagonal elem(works oonly for square matrix)
for i in range(0, 3):
    for j in range(0, 3):
        if i + j == len(list2D) - 1:
            print(list2D[i][j])

# to print rightmost column
for i in range(0, 3):
    for j in range(0, 3):
        if j == len(list2D) - 1:
            print(f"rightmost column element= {list2D[i][j]}")

# to print entire matrix
for i in range(0, 3):
    for j in range(0, 3):
        print(list2D[i][j], end=" ")
    print()
