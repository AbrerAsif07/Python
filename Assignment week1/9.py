length = float(input("ENter length of rectangle = "))
breadth = float(input("ENter breadth of rectangle = "))
area = length * breadth
if length == breadth:
    print(f"It is a square of area = {area} sq cm")
else:
    print(f"It is a rectangle of area = {area} cm sq")
