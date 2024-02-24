import re
import sys

def main():
    address = input("IPv4 Address: ")
    if validate(address):
        print("True")
    else:
        print("False")

def validate(ip):
    if re.search("^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        numbers = ip.split(".")
        for number in numbers:
            if int(number) < 0 or int(number) > 255:
                return False
        return True
    else :
        return False



if __name__ == "__main__":
    main()