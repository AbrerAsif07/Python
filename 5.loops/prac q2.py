str = int(input("Enter the start no = "))
end = int(input("Enter the end no = "))
count = 0
if str < end:
    i = str
    j = end
    while i <= j:
        if i % 3 == 0 and j % 5 == 0:
            count = count + 1
            i = i + 1
    print(count)

else:
    i = end
    j = str
    while i <= j:
        if i % 3 == 0 and j % 5 == 0:
            count = count + 1
            i = i + 1
    print(count)
