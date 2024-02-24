c = input("camelCase: ")
print("snake_case: ", end="")
for i in c:
    if i.islower():
        print(i, end="")
    elif i.isupper():
        print("_" + i.lower(), end="")
