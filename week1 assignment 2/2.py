v1 = int(input("Enter no of classes held = "))
v2 = int(input("Enter no of classes attended = "))
att_percent = (v2 / v1) * 100
if att_percent < 75:
    print(f"You are detained with percentsge of {att_percent} % ")
else:
    print(f"NOt detained w percent of {att_percent}%")
