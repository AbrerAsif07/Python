start = int(input("Enter start no: "))
end = int(input("Enter end no: "))
if start < end:
    i = start
    j = end
    while i <= j:
        print(i, end=" ")
        i = i + 1

else:
    i = end
    j = start
    while i <= j:
        print(j, end=" ")
        j = j - 1
