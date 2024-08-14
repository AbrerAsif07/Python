my_string = "ASHGddhuIdbuYSaug"
count = 0
for ch in my_string:
    ascii_conv = ord(ch)
    if ascii_conv > 97 and ascii_conv < 122:
        count += 1
print(f"The total no of smaller letters are {count}")

