def marks(s1, s2, s3, s4, s5) -> bool:
    total = (s1 + s2 + s3 + s4 + s5 / 500) * 100
    return total >= 33

    # if total < 33:
    #     return False
    # return True


print(marks(10, 20, 30, 40, 50))
