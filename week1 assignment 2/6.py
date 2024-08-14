n1 = int(input("enter no1 = "))
n2 = int(input("enter no2 = "))
n3 = int(input("enter no3 = "))
n4 = int(input("enter no4 = "))
# num1 = int(input("Enter the first number = "))
# num2 = int(input("Enter the second number = "))
# num3 = int(input("Enter the third number = "))
# num4 = int(input("Enter the fourth number = "))

if n1 < n2 and n1 < n3 and n1 < n4:
    smallest = n1
elif n2 < n1 and n2 < n3 and n2 < n4:
    smallest = n2
elif n3 < n1 and n3 < n2 and n3 < n4:
    smallest = n3
else:
    smallest = n4

print(f"The smallest number is {smallest}")
