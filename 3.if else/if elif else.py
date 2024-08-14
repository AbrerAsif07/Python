"""
Ask a mark from a user.

91 - 100 -> A
81 - 90 -> B
71 - 80 -> C
61 - 70 -> D
1 - 60 -> Fail
"""

val = int(input("Enter your marks = "))
if val >= 91 and val <= 100:
    print("A grade")
elif val >= 81 and val <= 90:
    print("b")
elif val >= 71 and val <= 80:
    print("c")
elif val >= 61 and val <= 70:
    print("c")
elif val >= 0 and val <= 60:
    print("fail")
else:
    print("INvalid")
