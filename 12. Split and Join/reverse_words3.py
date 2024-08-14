my_string = "python is a good language"
words = my_string.split()
print(words)
words.reverse()
print(words)

result = " ".join(word[::-1] for word in words)
print(result)
