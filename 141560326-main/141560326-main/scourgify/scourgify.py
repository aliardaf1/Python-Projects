import csv , sys

def main():
    check()

    my_list =[]

    try:
        with open(sys.argv[1] , "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"].split(",")
                my_list.append({"first" : name[1].lstrip(), "last" : name[0] , "house" : row['house']})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2] , "w") as second_file:
        writer = csv.DictWriter(second_file , fieldnames = ["first" , "last" ,"house"])
        writer.writerow({"first" : "first", "last" : "last" , "house" : "house"})
        for row in my_list:
            writer.writerow({"first" : row["first"], "last" : row["last"], "house" : row["house"]})

def check():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

if __name__ == "__main__" :
    main()