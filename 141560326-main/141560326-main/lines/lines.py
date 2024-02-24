import sys


def main():
    check()

    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
    except FileNotFoundError:
        sys.exit("File does not exist")

    number_of_lines = 0

    for line in lines:
        if (line.lstrip()).startswith("#") or line.isspace():
            continue
        else:
            number_of_lines += 1

    print(number_of_lines)


def check():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not (sys.argv[1]).endswith(".py"):
        sys.exit("Not a Python file")


if __name__ == "__main__":
    main()
