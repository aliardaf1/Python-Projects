import string
def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    sbeggining = s[0:2]
    illegal = False
    index = 0
    numberExist = False
    if len(s) > 6 or len(s) < 2 or sbeggining.isdecimal() or s.isspace() :
        return False
    else :
        srest = s[2:len(s)]
        for i in srest :
            if i.isdecimal():
                numberExist = True
                if i == '0':
                    k = 0
                    if index == 0 :
                        return False
                    while k < index :
                        if not srest[k].isdecimal():
                            return False
                        k+=1
                else :
                    illegal = True
            elif i.isalpha():
                if illegal or numberExist:
                    return False
            elif i in string.punctuation:
                return False
            index += 1
        return True

if __name__ == "__main__":
    main()