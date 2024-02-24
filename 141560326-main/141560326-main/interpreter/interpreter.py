expr = input("Expression:")
x , y , z = expr.split(" ")

if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "/":
     print(float(x) / float(z))
elif y == "*":
     print(float(x) * float(z))
