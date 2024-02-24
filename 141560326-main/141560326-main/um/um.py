import re


def main():
    print(count(input("Text: ")))


def count(s):
    ums = re.findall(r"\b\W*um\b\W*" , s, re.IGNORECASE)
    return len(ums)

if __name__ == "__main__":
    main()