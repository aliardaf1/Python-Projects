import inflect

p = inflect.engine()
names = []
while True :
    try :
        Input = input("Name: ")
        names.append(Input)
    except EOFError :
        print()
        break

if len(names) == 1 :
    print("Adieu, adieu, to " + names[0])
else :
    output = p.join(names)
    print("Adieu, adieu, to " + output)