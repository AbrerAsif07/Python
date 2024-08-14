val = int(input("Enter a no = "))
if val % 3 == 0 and val % 5 == 0:
    print("foobar")
elif val % 3 == 0:
    print("foo")
elif val % 5 == 0:
    print("bar")
else:
    print("INValid ")
