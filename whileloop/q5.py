"""
5674 to 10983 
kitne 
1.div by 7
2 div by 2 and 7
"""

count = 0
count1 = 0
i = 5674
j = 10983
while i <= j:
    if i % 7 == 0:
        count += 1
    if i % 7 == 0 and i % 2 == 0:
        count1 += 1
    i += 1
print(count)
print(count1)
