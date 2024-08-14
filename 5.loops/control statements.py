"continue exits everything wriiten after it and goes back into the loop"
"Break exits from the entire loop and stops"
# i = 1
# while i <= 3:
#     print("mc")
#     if i == 2:
#         continue
#     i = i + 1

# print("hello")
n = 368
total = 0
i = 1
while i <= n:
    if n % i == 0:
        total = total + i
    i = i + 1
print(total)
