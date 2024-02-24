dict = {}
while True:
    try :
        item = input().upper()
        if not item in dict :
            dict[item] = 1
        else :
            dict[item] += 1
    except KeyError :
        pass
    except EOFError :
        break

for keys in sorted(dict) :
    print(dict.get(keys) , keys)