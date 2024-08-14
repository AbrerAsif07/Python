def pattern(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()


x = int(input("Enter no of lines: "))
pattern(x)
