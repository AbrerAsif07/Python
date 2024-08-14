str = int(input("Enter the start no = "))
end = int(input("Enter the end no = "))

sum = 0
if str < end:
    i = str
    j = end
    while i <= j:
        sum = sum + i
        i = i + 1
    print(sum)
else:
    i = end
    j = str
    while i <= j:
        sum = sum + i
        i = i + 1
    print(sum)
