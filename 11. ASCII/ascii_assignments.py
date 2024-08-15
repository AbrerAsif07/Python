# Q1. Function to reverse a string
def reverse(str1: str):
    reverse_string = str1[::-1]
    print(reverse_string)


x = "asif"
reverse(x)


# Q2. Takes a string and returns in uppercase
def upp(str2: str):
    result = ""
    for ch in str2:
        if "a" <= ch <= "z":
            result += chr(ord(ch) - 32)
        else:
            result += ch
    return result


x = "asif barlaskar"
print(upp(x))

# Q3. Function to remove all vowels frm a string


def cons(str3: str):
    result = ""
    vowels = "aeiouAEIOU"
    for ch in str3:
        if ch not in vowels:
            result += ch
    return result


z = "asif"
print(cons(z))

# Q4. Function that counts the no of words from a given string


def count(str3: str):
    count = 0
    for ch in str3:
        if "a" <= ch <= "z":
            count += 1
        elif "A" <= ch <= "Z":
            count += 1
        elif ch == " ":
            count += 1
        else:
            print("Invalid")
    return count


x = "asif  barlaskar"
print(count(x))

# Q5. Word that returns the longest string from a word


