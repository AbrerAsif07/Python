def marks(n1: int, n2: int, n3: int, n4: int, n5: int):
    total = n1 + n2 + n3 + n4 + n5
    percentage = (total / 500) * 100
    print(f"The total percentage is {percentage:.2f}")


marks(10, 45, 55, 44, 69)
