# ask start no and end no from user and print from start to end
start = int(input("Enter first number: "))
end = int(input("Enter last number: "))
# Never change input paramters by user, create new variables and make changes necessary
i = start
j = end
if i < j:
    while i <= j:
        print(i, end=" ")
        i += 1
else:
    print("starting no is greater than end")
