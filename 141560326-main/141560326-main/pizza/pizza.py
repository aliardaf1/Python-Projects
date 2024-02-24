import sys , csv
from tabulate import tabulate

def main():
    check()

    my_list = []
    try:
        with open(sys.argv[1], "r") as file:
            row = csv.reader(file)
            for line in row:
                my_list.append(line)
    except FileNotFoundError :
        sys.exit("File does not exist")

    print(tabulate(my_list[1:], headers = my_list[0], tablefmt="grid"))
def check():
    if len(sys.argv) < 2 :
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2 :
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()