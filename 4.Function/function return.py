# Function with return statement means creating a variable return that is applicable to send to different blocks of nested function
# eg: TO add 2 nos and also to check if even or odd the sum is
def add(n1: int, n2: int):
    sum = n1 + n2
    return sum


def check(n): #Creating diff funcn block where previous result can be used
    if n % 2 == 0:
        print("even")
    else:
        print("odd")


x = add(2, 4) #user can call whichever funcn block ans he wants, also has to make a variable to return his ans
print(x)
check(x)
