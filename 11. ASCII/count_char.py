def countchar(string_1: str):
    alpha = 0
    digits = 0
    spaces = 0
    symbols = 0
    for ch in string_1:
        ascii_code = ord(ch)
        if ascii_code >= 97 and ascii_code <= 122:
            alpha += 1
        elif ascii_code >= 65 and ascii_code <= 200:
            alpha += 1
        elif ascii_code >= 48 and ascii_code <= 57:
            digits += 1
        elif ascii_code == 32:
            spaces += 1
        else:
            symbols += 1
    print(
        f" No of: alphabets= {alpha}, digits:{digits}, spaces={spaces} and symbols:{symbols} "
    )


my_string = "asifLAMAR123  @!"
countchar(my_string)
