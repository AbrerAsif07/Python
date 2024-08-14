my_marks = {
    "history": 69,
    "maths": 85,
    "english": 69,
    "hindi": 85,
}
print(my_marks.keys())
for k in my_marks.keys():
    print(k)

# To print only history from given dictionary
# print(my_marks.items()) " prints both keys and value pairs"
# to print only key values of 0th index convert it into list
result = my_marks.items()
print(result)
# print(list(result)[0][0]) 'it was convertedt to list as items returns set ie non indexable
