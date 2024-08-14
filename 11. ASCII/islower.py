def islower(string_1: str) -> bool:
    islower = False
    isupper = False
    for ch in string_1:
        ascii_code = ord(ch)
        if ascii_code > 97 and ascii_code < 122:
            islower = True
        elif ascii_code > 65 and ascii_code < 90:
            isupper = True
    if isupper == False and islower == True:
        return True
    return False


my_string = "dwijBc123"
print(islower(my_string))
