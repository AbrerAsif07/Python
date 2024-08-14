n1 = int(input("Enter 1st no = "))
n2 = int(input("Enter 2nd no = "))
op = str(input("what operation do u wnt to perform add,sub,mult,div = "))

if op == "add":
    result = n1 + n2
elif op == "sub":
    result = n1 - n2
elif op == "mult":
    result = n1 * n2
elif op == "div":
    if n2 != 0:
        result = n1 / n2
    else:
        print("invalid")

else:
    print("invalid")

print(result)
